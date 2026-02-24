# Extension Roadmap｜Six Killer Capabilities (Evidence-Only, No New Gates)

Sealed guarantees:
- GateVectorLen=91
- Fail-Closed never weakens
- extensions only add evidence fields (intent_audit_group / AuditCard_t)

---

## 1) Adaptive Risk Thresholds (Entropy Watchdog)
Use Ledger history to tighten τ_intent under slow-penetration patterns.

Evidence:
- `historical_risk_index`
- `tau_effective`
Audited every request.

---

## 2) ShadowOnly Decoy (Counter-Extraction Demonstration)
Under Fail-Closed, return ShadowOnly outputs plus a decoy fingerprint.

Evidence:
- `poison_tag`
- `decoy_hash`
- `decoy_payload` (minimal)

---

## 3) Cross-Device Continuity Enforcement
Block device-farm “handoff distillation”.

Evidence:
- `device_chain_hash`
- `session_binding`

---

## 4) Multi-Tenant / Multi-Model Isolation
Detect cross-model probing inside a shared platform.

Evidence:
- `tenant_id`
- `model_fingerprint`
- `cross_model_probe`

---

## 5) One-Click Holographic Audit Export
Produce regulator-grade AuditCard with replayable evidence keys.

Evidence:
- stable schema version
- replay keys: req_hash, gate hashes, ledger head hash

---

## 6) Low-Intent ZK (Placeholder Interface)
VIPs can supply a proof placeholder indicating low intent risk.

Evidence:
- `zk_low_intent_proof`
- `zk_verify_result`

---

**Signature**: Liangfeng Hu | YFCore Technology Limited
