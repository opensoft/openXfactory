"""THE HOST'S BINDING-TRUST POLICY (plan 034 T094; #1144 16.3a, T007 batch M;
RULED `#656` comment `5962785556`, item 2, and the policy RULED on `#656`
comment `5970369724`, *"Governance approval (Recommended)"*).

From T100, openDox reads a served repository's model bindings through a trust
seam, `opendox.doxbench_trust`, whose neutral default trusts only what the
operator recorded on this machine and refuses the console intake's broker. A
host's registration wins. openxFactory registers `GovernedBindingTrust` in
`opendox_host.register_openxfactory()`, so its governed flow is what it was
before T100: a binding whose declaration is pending is refused, as the port
factory already passes over it, and every other binding of the served checkout
is trusted. These cases pin the registration, each verdict, that nothing is
written to the operator's state, and the port the factory resolves, against
openDox's strict default in the same checkout.
"""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

import pytest

import opendox_host
from opendox import doxbench_binding as binding_mod
from opendox import doxbench_install as install_mod
from opendox import doxbench_intake as intake_mod
from opendox import doxbench_trust as trust_mod

BINDING_ID = "governed-model"


def _record() -> dict:
    """A binding that takes no credential (auth kind `none`), so no case here
    needs a broker, a secret or a listener to tell the verdicts apart."""
    return {"kind": "model-provider-binding", "id": BINDING_ID,
            "label": "Governed model", "provider": "anyone",
            "auth_kind": "none", "approved_by": "brett",
            "endpoint": "https://models.example.invalid/v1",
            "dialect": "openai-chat-v1", "model": None,
            "credential_ref": None, "broker_argv": []}


def _binding():
    return binding_mod.ModelProviderBinding.from_record(_record())


def _repository(tmp_path: Path) -> Path:
    root = tmp_path / "governed"
    root.mkdir()
    env = {k: v for k, v in os.environ.items()
           if not k.startswith(("GIT_", "XF_"))}
    subprocess.run(["git", "init", "-q", str(root)], check=True, env=env)
    path = binding_mod.bindings_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"schema_version": 1,
                                "kind": "model-provider-bindings",
                                "bindings": [_record()]}), encoding="utf-8")
    return root


def _propose(root: Path) -> intake_mod.DeclarationStore:
    store = intake_mod.DeclarationStore(intake_mod.declarations_path(root))
    store.propose(intake_mod.ModelDeclaration(
        binding_id=BINDING_ID, status=intake_mod.STATUS_PENDING,
        install_posture=intake_mod.POSTURE_SINGLE_OPERATOR,
        proposed_by="brett@opensoft.one", proposed_at=intake_mod.stamp()))
    return store


def _approve(root: Path) -> None:
    _propose(root).approve(BINDING_ID, issued_by="console",
                           approved_by="brett",
                           expires_at=intake_mod.approval_expiry(),
                           audit_ref="opaud-governed-1")


def test_the_registered_policy_is_this_hosts_own():
    """`register_openxfactory()` ran at process start (the conftests), so the
    seam answers this host's policy and openDox's consumers read it, not
    their lazily registered default."""
    policy = opendox_host.binding_trust_policy()
    assert trust_mod.current() is policy
    assert trust_mod.policy() is policy
    # Idempotent: this host's own object again is a no-op.
    assert trust_mod.register(policy) is policy
    with pytest.raises(trust_mod.TrustPolicyAlreadyRegistered):
        trust_mod.register(trust_mod.MachineTrust())


@pytest.mark.parametrize("declared", ["undeclared", "approved"])
def test_an_undeclared_or_approved_binding_is_trusted(tmp_path, declared):
    root = _repository(tmp_path)
    if declared == "approved":
        _approve(root)
    verdict = opendox_host.binding_trust_policy().verdict(_binding(), root=root)
    assert verdict.trusted and verdict.admits(_binding())
    assert verdict.basis == trust_mod.BASIS_HOST


def test_a_pending_binding_is_refused_with_the_governed_reason(tmp_path):
    root = _repository(tmp_path)
    _propose(root)
    verdict = opendox_host.binding_trust_policy().verdict(_binding(), root=root)
    assert not verdict.trusted
    assert verdict.reason == opendox_host.GOVERNED_PENDING_REASON
    with pytest.raises(trust_mod.BindingUntrusted) as refused:
        trust_mod.require_admitted(_binding(), verdict)
    assert BINDING_ID in str(refused.value)


def test_an_unreadable_declarations_document_admits_nothing(tmp_path):
    root = _repository(tmp_path)
    path = intake_mod.declarations_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("schema_version: [unclosed\n", encoding="utf-8")
    verdict = opendox_host.binding_trust_policy().verdict(_binding(), root=root)
    assert not verdict.trusted
    assert "cannot be read" in verdict.reason


def test_recording_writes_nothing_to_the_operators_state(tmp_path, monkeypatch):
    """The governed record is the gate's: `add`, `edit` and `set-credential`
    ask `record()`, which answers the verdict and writes no trust file."""
    state = tmp_path / "state"
    monkeypatch.setenv("OPENDOX_STATE_DIR", str(state))
    root = _repository(tmp_path)
    verdict = opendox_host.binding_trust_policy().record(_binding(), root=root)
    assert verdict.trusted
    assert not state.exists()


def test_the_port_factory_resolves_the_binding_and_the_default_would_not(
        tmp_path, monkeypatch):
    """Through the one place a binding becomes usable,
    `declared_model_port_factory`: under this host's policy an undeclared
    binding of the served checkout resolves a usable port, as before T100.
    Under openDox's strict default, in the same checkout and process, it
    resolves the refusing `UntrustedBindingPort` until the operator trusts it
    on this machine. The host's registration is restored afterwards."""
    monkeypatch.setenv("OPENDOX_STATE_DIR", str(tmp_path / "state"))
    root = _repository(tmp_path)
    sessions = tmp_path / "sessions"
    port = install_mod.declared_model_port_factory(
        sessions, checkout_root=root)()
    assert not isinstance(port, trust_mod.UntrustedBindingPort), port
    policy = opendox_host.binding_trust_policy()
    trust_mod.unregister()
    try:
        trust_mod.register(trust_mod.MachineTrust(state_dir=tmp_path / "st"))
        refused = install_mod.declared_model_port_factory(
            sessions, checkout_root=root)()
        assert isinstance(refused, trust_mod.UntrustedBindingPort), refused
    finally:
        trust_mod.unregister()
        trust_mod.register(policy)
    assert trust_mod.current() is policy


def test_the_console_intake_is_offered_and_admits_a_new_binding(tmp_path):
    """The console intake asks its OWN question, apart from any binding's trust
    (`doxbench_trust.intake_verdict_for`, which `serve_workbench`'s intake
    hand-off asks), and openDox offers the intake only where the registered
    policy answers `intake_verdict` (`intake_admissible`; openDox-code's T100
    follow-on, A5). The binding the intake declares is undeclared while its
    broker runs (its PENDING declaration is written after the hand-off), so
    this host admits it, where openDox's default refuses every intake
    (`INTAKE_BROKER_UNTRUSTED`). A binding already pending is refused with the
    governed reason, and a declarations document that cannot be read admits
    nothing (RULED `5970369724`: the governed flow, "the console intake
    included, stays as it is")."""
    root = _repository(tmp_path)
    assert trust_mod.intake_admissible()
    verdict = trust_mod.intake_verdict_for(_binding(), root=root)
    assert verdict.admits(_binding())
    assert verdict.basis == trust_mod.BASIS_HOST
    _propose(root)
    pending = trust_mod.intake_verdict_for(_binding(), root=root)
    assert not pending.trusted
    assert pending.reason == opendox_host.GOVERNED_PENDING_REASON
    intake_mod.declarations_path(root).write_text(
        "schema_version: [unclosed\n", encoding="utf-8")
    unreadable = trust_mod.intake_verdict_for(_binding(), root=root)
    assert not unreadable.trusted
    assert "cannot be read" in unreadable.reason
