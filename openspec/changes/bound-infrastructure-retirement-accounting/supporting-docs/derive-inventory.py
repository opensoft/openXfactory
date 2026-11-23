"""Reproduce a planning inventory; optional baseline parsers do not authenticate it."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
NETWORK = "Microsoft.Network"
REGISTRATION = "registration"
CLEANUP = "cleanup"
OBSERVATION = "observation"
POOLS = (REGISTRATION, CLEANUP, OBSERVATION)
GROUPS = ("private", "arm", "namespace", "journal")
PATH_FIELD = "resource_path"
DEPS_FIELD = "dependency_paths"
ROLES = ("control", "gate", "worker")
KINDS = {
    "vm": ("Microsoft.Compute", "virtualMachines", "vm"),
    "os_disk": ("Microsoft.Compute", "disks", "osdisk"),
    "nic": (NETWORK, "networkInterfaces", "nic"),
    "public_ip": (NETWORK, "publicIPAddresses", "pip"),
    "vnet": (NETWORK, "virtualNetworks", "vnet"),
    "nsg": (NETWORK, "networkSecurityGroups", "nsg"),
}
PARENT = ("/subscriptions/297b2389-33bf-48c8-8deb-0b92838431e4/"
          "resourceGroups/rg-opensoft-wallet-mfa-qa")
RECORDS = ("reservation", "provisioned", "final_link", "setup_receipt", "run_receipt")


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode()


def unique_pairs(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("duplicate-key")
        value[key] = item
    return value


def resource_path(kind, role=""):
    provider, resource_type, prefix = KINDS[kind]
    suffix = "-" + role if role else ""
    name = prefix + "-wallet-mfa" + suffix + "-qa-01"
    return PARENT + "/providers/" + provider + "/" + resource_type + "/" + name


def roles_for(kind):
    if kind in ("vm", "os_disk", "nic", "nsg"):
        return ROLES
    if kind == "public_ip":
        return ("control",)
    return ("",)


def dependencies(kind, role):
    if kind in ("os_disk", "nic"):
        return [resource_path("vm", role)]
    if kind == "public_ip":
        return [resource_path("nic", "control")]
    if kind == "vnet":
        return [resource_path("nic", item) for item in ROLES]
    if kind == "nsg":
        return [resource_path("nic", role), resource_path("vnet")]
    return []


def graph_resources():
    nodes = []
    for kind in KINDS:
        for role in roles_for(kind):
            scope = role or "pilot"
            nodes.append({
                PATH_FIELD: resource_path(kind, role), "kind": kind,
                DEPS_FIELD: sorted(dependencies(kind, role), key=str.lower),
                "resource_policy_ref": "policy:" + kind + ":" + scope,
                "create_attempt_ref": "create:" + kind + ":" + scope,
                "disposition": "ephemeral",
            })
    return sorted(nodes, key=lambda node: node[PATH_FIELD].lower())


def cost_row(name, private=0, arm=0, namespace=0, journal=0,
             basis="proposed schedule"):
    return {"name": name, "private": private, "arm": arm, "namespace": namespace,
            "journal": journal, "basis": basis}


def schedule_rows(node_count, edge_count):
    return {
        REGISTRATION: [
            cost_row("selected authority and source", private=8),
            cost_row("namespace exact-set inspection", namespace=2 * node_count),
            cost_row("one registration claim and acknowledged readback", journal=6),
            cost_row("P02 reservation sensitivity allowance; no authorization to rerun P02",
                     namespace=node_count + 3,
                     basis="existing source formula; separately owned P02 normally outside P07"),
            cost_row("genuine run-link registration", private=6,
                     namespace=2 * node_count, journal=4),
        ],
        CLEANUP: [
            cost_row("close write/run admission", private=4, journal=4),
            cost_row("per-kind retirement core", private=9 * node_count + edge_count,
                     arm=3 * node_count + edge_count,
                     namespace=14 * node_count + 2 * edge_count,
                     basis="conservative sum of measured old per-resource costs; historical receipt-cache reuse can only lower this line"),
            cost_row("distinct historic creation terminal receipts", private=node_count,
                     basis="existing source upper bound"),
            cost_row("at most three original-create and three original-delete polls per resource",
                     private=6 * node_count, arm=6 * node_count,
                     basis="proposed finite original-operation schedule, never a resend"),
            cost_row("uncertain conditional-write read-only reloads", namespace=2 * node_count,
                     basis="existing source upper bound: one reload per each of two transitions"),
            cost_row("same-owner original-state reconstruction",
                     namespace=4 * node_count, journal=2 * node_count),
            cost_row("new action/terminal bookkeeping", journal=4 * node_count + 8),
            cost_row("owner plus at most three duplicate trigger deliveries", private=4, journal=12),
            cost_row("two current outcome reads for at most sixteen actual registered credentials",
                     private=32),
        ],
        OBSERVATION: [
            cost_row("independent current resource absence", private=node_count,
                     arm=node_count, namespace=2 * node_count),
            cost_row("twelve retained ARM objects and three protected-state objects",
                     private=12, arm=12, namespace=6),
            cost_row("independent current refusal evidence for actual registered credentials", private=16),
            cost_row("current observer identity and authority", private=4),
            cost_row("original operation and exact-set crosscheck",
                     private=node_count, namespace=2 * node_count),
            cost_row("immutable final result and independent audit", private=4, journal=4),
        ],
    }


def load_records(directory):
    records = {}
    for name in RECORDS:
        raw = (directory / (name + ".json")).read_bytes()
        if len(raw) > 16384:
            raise ValueError("fixture-size")
        value = json.loads(raw, object_pairs_hook=unique_pairs)
        if not isinstance(value, dict) or canonical(value) != raw:
            raise ValueError("fixture-canonical")
        records[name] = raw
    return records


def validate_records(records, expected):
    if set(records) != set(RECORDS) or set(expected) != set(RECORDS):
        raise ValueError("fixture-set")
    measured = {}
    for name, raw in records.items():
        measured[name] = {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}
    if measured != expected:
        raise ValueError("recorded-fixture-mismatch")
    return measured


def verify_source_files(root, hashes):
    for relative, expected in hashes.items():
        if hashlib.sha256((root / relative).read_bytes()).hexdigest() != expected:
            raise ValueError("inventory-source-mismatch: " + relative)


def verify_baseline(root, records, hashes):
    """Only this explicit option repeats the actual unchanged closed parsers."""
    verify_source_files(root, hashes)
    sys.path[:0] = [str(root / "scripts"), str(root / "tests")]
    from workload_factory_binding_runtime.azure_composition import selection
    from runtime_binding import test_azure_namespace as baseline

    reserved = selection.reservation(records["reservation"],
                                     approved=records["reservation"])
    deployed = selection.provisioned(records["provisioned"], reserved=reserved,
                                    authenticated_readback=records["provisioned"])
    linked = baseline.linked(deployed)
    if linked.raw != records["final_link"]:
        raise ValueError("baseline-final-link")
    for run in (False, True):
        _, authority, _, _ = baseline.receipt(reserved, run=run)
        name = "run_receipt" if run else "setup_receipt"
        arguments = {"deployed": deployed, "linked": linked} if run else {}
        result = selection.retirement(records[name], reserved=reserved,
                                      authority=authority, **arguments)
        if result.raw != records[name]:
            raise ValueError("baseline-retirement")


def derive(inputs, records):
    """Validate recorded bytes and recompute every modeled graph/call total."""
    value = copy.deepcopy(inputs)
    expected = value.pop("recorded_parser_fixtures")
    scope = value.pop("graph_scope")
    measured = validate_records(records, expected)
    resources = graph_resources()
    node_count = len(resources)
    edge_count = sum(len(item[DEPS_FIELD]) for item in resources)
    value["graph"] = {"ephemeral_count": node_count, "dependency_edges": edge_count,
                      "resources": resources, **scope}
    rows = schedule_rows(node_count, edge_count)
    for items in rows.values():
        facade = sum(item["namespace"] + item["journal"] for item in items)
        items.append(cost_row(
            "authenticated state-facade exchanges, one per modeled namespace/journal backend call",
            private=facade,
            basis="proposed conservative remote-facade schedule; backend calls remain separately counted"))
    totals = {pool: {group: sum(row[group] for row in items) for group in GROUPS}
              for pool, items in rows.items()}
    limits = value["selected_limits"]
    if set(limits) != set(POOLS):
        raise ValueError("pool-set")
    for pool in POOLS:
        if set(limits[pool]) != set(GROUPS):
            raise ValueError("group-set")
        for group in GROUPS:
            limit = limits[pool][group]
            if type(limit) is not int or limit < totals[pool][group]:
                raise ValueError("modeled-cost-exceeds-limit")
    value["rows"] = rows
    value["modeled_totals"] = totals
    value["whole_modeled"] = {group: sum(totals[p][group] for p in POOLS)
                              for group in GROUPS}
    value["whole_limits"] = {group: sum(limits[p][group] for p in POOLS)
                             for group in GROUPS}
    value["parser_fixture_measurement"] = {
        "kind": ("recorded baseline closed-parser acceptance; default reproduction "
                 "checks exact canonical fixture bytes and arithmetic; --adapter-root "
                 "repeats actual baseline parsers; none is authenticated service provenance"),
        "records": measured, "all_under_existing_16384_cap": True,
    }
    return value


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--adapter-root", type=Path,
                        help="also verify all recorded source hashes and repeat actual baseline parsers")
    args = parser.parse_args(argv)
    try:
        inputs = json.loads((HERE / "inventory-inputs.json").read_text(),
                            object_pairs_hook=unique_pairs)
        records = load_records(HERE / "fixtures")
        result = derive(inputs, records)
        if args.adapter_root is not None:
            verify_baseline(args.adapter_root.resolve(), records,
                            inputs["basis"]["parser_inputs_sha256"])
    except (OSError, ValueError):
        print("inventory-refused", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
