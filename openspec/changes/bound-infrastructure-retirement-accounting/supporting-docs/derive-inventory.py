"""Planning arithmetic and unchanged-parser fixtures; never runtime qualification."""
from pathlib import Path
import sys,json,hashlib
import argparse
parser=argparse.ArgumentParser(description="Derive the source-planning inventory and synthetic closed-record sizes; no provider I/O.")
parser.add_argument("--adapter-root",type=Path,required=True)
W=parser.parse_args().adapter_root.resolve()
sys.path[:0]=[str(W/"scripts"),str(W/"tests")]
from workload_factory_binding.evidence import canonical
from workload_factory_binding_runtime.azure_composition import selection as s
from runtime_binding import test_azure_namespace as n
parent="/subscriptions/297b2389-33bf-48c8-8deb-0b92838431e4/resourceGroups/rg-opensoft-wallet-mfa-qa"
types={"vm":("Microsoft.Compute","virtualMachines"),"os_disk":("Microsoft.Compute","disks"),"nic":("Microsoft.Network","networkInterfaces"),"public_ip":("Microsoft.Network","publicIPAddresses"),"vnet":("Microsoft.Network","virtualNetworks"),"nsg":("Microsoft.Network","networkSecurityGroups")}
roles=("control","gate","worker")
def path(kind,role=""):
 provider,typ=types[kind]
 name={"vm":"vm","os_disk":"osdisk","nic":"nic","public_ip":"pip","vnet":"vnet","nsg":"nsg"}[kind]+"-wallet-mfa"+("-"+role if role else "")+"-qa-01"
 return parent+"/providers/"+provider+"/"+typ+"/"+name
nodes=[]
for kind in types:
 for role in (roles if kind in ("vm","os_disk","nic","nsg") else (("control",) if kind=="public_ip" else ("",))):
  deps=([path("vm",role)] if kind in ("os_disk","nic") else [path("nic","control")] if kind=="public_ip" else [path("nic",x) for x in roles] if kind=="vnet" else [path("nic",role),path("vnet")] if kind=="nsg" else [])
  nodes.append({"resource_path":path(kind,role),"kind":kind,"dependency_paths":sorted(deps,key=str.lower),"resource_policy_ref":"policy:"+kind+":"+(role or "pilot"),"create_attempt_ref":"create:"+kind+":"+(role or "pilot"),"disposition":"ephemeral"})
nodes.sort(key=lambda x:x["resource_path"].lower())
N=len(nodes);D=sum(len(x["dependency_paths"]) for x in nodes)
assert (N,D)==(14,16)
v=n.vector()
v.update(target={"tenant_id":"74ce1e7d-7455-4694-b00d-9ac83c6821ce","subscription_id":"297b2389-33bf-48c8-8deb-0b92838431e4","region":"westus","parent_paths":[parent]},resources=nodes)
r=s.reservation(canonical(v),approved=canonical(v));dep=n.deployed(r);linked=n.linked(dep)
fixtures={"reservation":r.raw,"provisioned":dep.raw,"final_link":linked.raw}
for run in (False,True):
 value,a,d,l=n.receipt(r,run=run)
 result=s.retirement(canonical(value),reserved=r,authority=a,**({"deployed":d,"linked":l} if run else {}))
 fixtures["run_receipt" if run else "setup_receipt"]=result.raw
def row(name,private=0,arm=0,namespace=0,journal=0,basis="proposed schedule"):
 return dict(name=name,private=private,arm=arm,namespace=namespace,journal=journal,basis=basis)
rows={
"registration":[row("selected authority and source",private=8),row("namespace exact-set inspection",namespace=2*N),row("one registration claim and acknowledged readback",journal=6),row("P02 reservation sensitivity allowance; no authorization to rerun P02",namespace=N+3,basis="existing source formula; separately owned P02 normally outside P07"),row("genuine run-link registration",private=6,namespace=2*N,journal=4)],
"cleanup":[row("close write/run admission",private=4,journal=4),row("per-kind retirement core",private=9*N+D,arm=3*N+D,namespace=14*N+2*D,basis="conservative sum of measured old per-resource costs; historical receipt-cache reuse can only lower this line"),row("distinct historic creation terminal receipts",private=N,basis="existing source upper bound"),row("at most three original-create and three original-delete polls per resource",private=6*N,arm=6*N,basis="proposed finite original-operation schedule, never a resend"),row("uncertain conditional-write read-only reloads",namespace=2*N,basis="existing source upper bound: one reload per each of two transitions"),row("same-owner original-state reconstruction",namespace=4*N,journal=2*N),row("new action/terminal bookkeeping",journal=4*N+8),row("owner plus at most three duplicate trigger deliveries",private=4,journal=12),row("two current outcome reads for at most sixteen actual registered credentials",private=32)],
"observation":[row("independent current resource absence",private=N,arm=N,namespace=2*N),row("twelve retained ARM objects and three protected-state objects",private=12,arm=12,namespace=6),row("independent current refusal evidence for actual registered credentials",private=16),row("current observer identity and authority",private=4),row("original operation and exact-set crosscheck",private=N,namespace=2*N),row("immutable final result and independent audit",private=4,journal=4)]}
for values in rows.values():
 values.append(row("authenticated state-facade exchanges, one per modeled namespace/journal backend call",private=sum(x["namespace"]+x["journal"] for x in values),basis="proposed conservative remote-facade schedule; backend calls remain separately counted"))
limits={"registration":{"private":128,"arm":0,"namespace":128,"journal":32},"cleanup":{"private":768,"arm":160,"namespace":512,"journal":128},"observation":{"private":192,"arm":48,"namespace":128,"journal":32}}
totals={pool:{k:sum(x[k] for x in values) for k in ("private","arm","namespace","journal")} for pool,values in rows.items()}
assert all(totals[p][k]<=limits[p][k] for p in limits for k in limits[p])
whole={k:sum(limits[p][k] for p in limits) for k in ("private","arm","namespace","journal")}
modeled={k:sum(totals[p][k] for p in totals) for k in whole}
record={
"classification":"source planning inventory and conservative schedule; not a measured full P07 runtime positive",
"date":"2026-11-23 America/La_Paz",
"basis":{"adapter":"b39feb3a5e9c30f25b28eb55751beb2ad4ff3e87","factory":"afb20ce1df21199e75550e48732b56ee67069c51","provider_sha256":hashlib.sha256((W/"scripts/workload_factory_binding_runtime/azure_composition/provider.py").read_bytes()).hexdigest(),"namespace_sha256":hashlib.sha256((W/"scripts/workload_factory_binding_runtime/azure_composition/namespace.py").read_bytes()).hexdigest()},
"selection":"proposed source refinement of S1: three role-specific NSGs; not deployed IDs or create authority",
"graph":{"ephemeral_count":N,"dependency_edges":D,"resources":nodes,"retained_ARM_observation_slots":["control-data-disk","gate-data-disk","measured-managed-image","credential-vault","redacted-evidence-storage","watchdog-function","watchdog-plan","watchdog-storage","watchdog-identity","disposable-parent-RG","retained-parent-RG","watchdog-parent-RG"],"protected_state_observation_slots":["permanent-namespace-catalog","retained-registration/action-state","retained-runtime-authority/replay-state"],"registered_credential_handle_cap":16},
"rows":rows,"modeled_totals":totals,"selected_limits":limits,"whole_modeled":modeled,"whole_limits":whole,
"application_byte_limits":{"registration":1048576,"cleanup":12582912,"observation":3145728,"whole":16777216,"scope":"complete application request/response bytes, including metadata and backend state; existing individual body caps remain"},
"time_limits":{"registration_transaction_seconds":30,"cleanup_original_seconds":300,"observation_original_seconds":60,"per_call_seconds":10,"current_observation_max_validity_seconds":60,"original_absolute_cleanup_deadline":"independently approved and clipping; never extended by this policy","registration_absolute_window":"existing approved maximum 86400 seconds; no UTC window selected"},
"parser_fixture_measurement":{"kind":"complete synthetic closed-record serialization only; parser equality is not authenticated service provenance","records":{name:{"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()} for name,raw in fixtures.items()},"all_under_existing_16384_cap":all(len(raw)<=16384 for raw in fixtures.values())},
"remaining_runtime_gate":"after exact source ratification: actual full-graph positive, physical/nested call accounting, real clocks, privacy, crash/refusal controls, full/native/hosted qualification and independent cleanup",
"operations":{"setup_dispatch":"unauthorized","feedback":"deferred","blocked_writes":"unreplayed"}}
print(json.dumps(record,indent=2))
