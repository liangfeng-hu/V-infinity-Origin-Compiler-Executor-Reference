import json
import time
import hashlib
from dataclasses import dataclass, asdict
from typing import Dict, Any

from reference_impl_import_fix import gate91, lse


def _now_ms() -> int:
    return int(time.time() * 1000)


def _sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


@dataclass
class AuditCard:
    t_ms: int
    req_id: str
    gatevector_len: int
    lse_budget_ok: bool
    seed_continuity_ok: bool
    i_90: int
    i_91: int
    i_flow: str
    commit_unique: int
    world_writeback: int
    out_level: str
    reason_code: str
    evidence_keys: Dict[str, str]
    intent_audit_group: Dict[str, Any]


def gate90_awake_score(req: Dict[str, Any], ledger: lse.InMemoryLedger) -> Dict[str, Any]:
    ig = req.get("intent_audit_group", {})
    seed = req.get("seed_continuity", {})

    base_tau = float(ig.get("base_tau", 0.65))
    hist_risk = ledger.historical_risk_index()
    tau_effective = base_tau * (1.0 + 0.20 * hist_risk)

    risk_score = float(ig.get("distillation_risk_score", 0.0))
    seed_ok = bool(seed.get("seed_continuity_ok", False))

    flags = ig.get("extraction_pattern_flags", {})
    device_chain_hash = ig.get("device_chain_hash", "")

    if ig.get("scenario") == "DEVICE_HOP" and not device_chain_hash:
        risk_score = max(risk_score, 0.90)

    cross_model_probe = bool(flags.get("cross_model_probe", False))
    federated_aggregation = bool(flags.get("federated_aggregation", False))

    passed = (risk_score < tau_effective) and seed_ok and (not cross_model_probe) and (not federated_aggregation)
    i_90 = 0 if passed else 1

    return {
        "i_90": i_90,
        "intent_risk_score": risk_score,
        "tau_effective": tau_effective,
        "seed_continuity_ok": seed_ok,
        "extraction_pattern_flags": flags,
        "device_chain_hash": device_chain_hash,
    }


def bus_decide(req_id: str, req: Dict[str, Any], ledger: lse.InMemoryLedger):
    gatevector_len = 91

    g90 = gate90_awake_score(req, ledger)
    g91v = gate91.evaluate_gate91(req_id, req.get("physical_proof", {}))

    intent_ok = (g90["i_90"] == 0)
    temporal_ok = bool(req.get("seed_continuity", {}).get("seed_continuity_ok", False))
    physical_ok = (g91v.i_91 == 0)

    lsev = lse.evaluate_lse(ledger, intent_ok, temporal_ok, physical_ok)

    commit_unique = 1 if lsev.i_lse == "0" else 0
    world_writeback = 1 if commit_unique == 1 else 0

    if lsev.i_lse == "0":
        payload = {"result": "ALLOW", "message": "I_FLOW=0", "commit_unique": 1, "world_writeback": 1}
        reason_code = "PASS"
        out_level = "Normal"
        ledger.append(lse.LedgerEvent(req_id=req_id, event="PASS", data={"i_flow": "0"}))
        i_flow = "0"
    else:
        out_level = req.get("out_level", "ShadowOnly")
        if lsev.reason_code == "RC_LSE_BUDGET_FAIL":
            reason_code = "RC_LSE_BUDGET_FAIL"
        elif g91v.i_91 != 0:
            reason_code = "RC_THERMO_FORGERY"
        else:
            reason_code = "RC_INTENT_OR_SEED_FAIL"

        decoy = None
        if out_level == "ShadowOnly":
            poison_tag = f"POISON_{req_id[-6:]}"
            decoy = {
                "poison_tag": poison_tag,
                "decoy_hash": _sha("DECOY:" + poison_tag),
                "decoy_payload": f"[HIGH_FIDELITY_OUTPUT_BUT_POISONED:{poison_tag}]",
            }
            ledger.append(lse.LedgerEvent(req_id=req_id, event="DISTILL_ALERT", data=decoy))

        payload = {
            "result": "BLOCK",
            "message": "Fail-Closed: ΔΩ=0, CommitUnique=0",
            "commit_unique": 0,
            "world_writeback": 0,
            "out_level": out_level,
            "reason_code": reason_code,
            "decoy": decoy,
        }
        ledger.append(lse.LedgerEvent(req_id=req_id, event="FAIL_CLOSED", data={"reason": reason_code}))
        i_flow = "+inf"

    evidence_keys = {
        "ledger_head_hash": ledger.head_hash(),
        "req_hash": _sha(json.dumps(req, sort_keys=True)),
        "gate90_hash": _sha(json.dumps(g90, sort_keys=True)),
        "gate91_hash": _sha(json.dumps(gate91.to_dict(g91v), sort_keys=True)),
    }

    audit = AuditCard(
        t_ms=_now_ms(),
        req_id=req_id,
        gatevector_len=gatevector_len,
        lse_budget_ok=lsev.budget_ok,
        seed_continuity_ok=bool(req.get("seed_continuity", {}).get("seed_continuity_ok", False)),
        i_90=g90["i_90"],
        i_91=g91v.i_91,
        i_flow=i_flow,
        commit_unique=commit_unique,
        world_writeback=world_writeback,
        out_level=out_level if i_flow != "0" else "Normal",
        reason_code=reason_code,
        evidence_keys=evidence_keys,
        intent_audit_group=req.get("intent_audit_group", {}),
    )

    return payload, audit


def scenario_ok():
    return {
        "intent_audit_group": {
            "scenario": "OK",
            "base_tau": 0.65,
            "distillation_risk_score": 0.10,
            "extraction_pattern_flags": {"cross_model_probe": False, "federated_aggregation": False},
            "device_chain_hash": "DEVCHAIN_OK",
        },
        "seed_continuity": {"seed_continuity_ok": True},
        "physical_proof": {"thermo_proof_ok": True, "attestation_ok": True},
        "out_level": "Normal",
    }


def scenario_distill_probe():
    return {
        "intent_audit_group": {
            "scenario": "DISTILL_PROBE",
            "base_tau": 0.65,
            "distillation_risk_score": 0.92,
            "extraction_pattern_flags": {"cross_model_probe": False, "federated_aggregation": False},
            "device_chain_hash": "DEVCHAIN_OK",
        },
        "seed_continuity": {"seed_continuity_ok": True},
        "physical_proof": {"thermo_proof_ok": True, "attestation_ok": True},
        "out_level": "ShadowOnly",
    }


def scenario_thermo_forgery():
    return {
        "intent_audit_group": {
            "scenario": "THERMO_FORGERY",
            "base_tau": 0.65,
            "distillation_risk_score": 0.20,
            "extraction_pattern_flags": {"cross_model_probe": False, "federated_aggregation": False},
            "device_chain_hash": "DEVCHAIN_OK",
        },
        "seed_continuity": {"seed_continuity_ok": True},
        "physical_proof": {"thermo_proof_ok": False, "attestation_ok": False},
        "out_level": "ShadowOnly",
    }


def scenario_device_hop_attack():
    return {
        "intent_audit_group": {
            "scenario": "DEVICE_HOP",
            "base_tau": 0.65,
            "distillation_risk_score": 0.20,
            "extraction_pattern_flags": {"cross_model_probe": False, "federated_aggregation": False},
            "device_chain_hash": "",
        },
        "seed_continuity": {"seed_continuity_ok": True},
        "physical_proof": {"thermo_proof_ok": True, "attestation_ok": True},
        "out_level": "ShadowOnly",
    }


def main():
    ledger = lse.InMemoryLedger()
    cases = [
        ("A_OK", scenario_ok),
        ("B_DISTILL", scenario_distill_probe),
        ("C_THERMO_FORGERY", scenario_thermo_forgery),
        ("D_DEVICE_HOP", scenario_device_hop_attack),
    ]

    for name, fn in cases:
        req_id = _sha(name + str(_now_ms()))[:16]
        req = fn()
        payload, audit = bus_decide(req_id, req, ledger)

        print("\n==============================")
        print(f"CASE: {name}  req_id={req_id}")
        print("------------------------------")
        print("PAYLOAD:")
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        print("------------------------------")
        print("AUDIT_CARD:")
        print(json.dumps(asdict(audit), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
