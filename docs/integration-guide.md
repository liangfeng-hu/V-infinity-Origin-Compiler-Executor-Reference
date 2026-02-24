# Integration Guide｜V∞ Constitutional AIOS Bus (V∞.1)

**Goal:** integrate the V∞ bus as a physical root-of-trust needle-eye so that **any world writeback** must be causally and physically anchored.

**Rules:** no new gates; add evidence fields only; Fail-Closed never weakens; CommitUnique is the only needle-eye; every verdict is audit-replayable.

---

## 1) Three Zero-Friction Integration Modes

### Mode A — Pre-Commit Sidecar (Recommended)
Inference Service → **V∞ Sidecar (LSE×Gate90×Gate91)** → Verdict → Output Router

- send only evidence fields: `intent_audit_group`, `seed_continuity`, `physical_proof`
- default: do **not** send raw prompt/completion (Mother Law 9: minimal leakage)
- sidecar always outputs: `payload` + `AuditCard_t`

Use when: you want the fastest “2-minute CISO proof” of Fail-Closed semantics.

### Mode B — Agent Runtime Needle-Eye (World-Writeback Control)
Before an agent executes any external action (payments, infra control, procurement):
1) build evidence from the proposed action plan (as evidence fields)
2) call the V∞ bus
3) only if CommitUnique=1 allow ΔΩ≠0

Fail → **SafeHold**: record evidence, execute nothing.

Use when: agent actions can cause irreversible consequences.

### Mode C — Platform Bus Service (Enterprise Standard)
Central “V∞ Bus Service” used by all models/agents/tenants:
- unified AuditCard schema
- unified Ledger and export
- bypass paths are unconstitutional → forced Fail-Closed

Use when: you need architecture committee approval, platform governance, and regulator-grade audit exports.

---

## 2) Minimal Data (Mother Law 9)
- transmit hashes, canonicalized telemetry, and `intent_audit_group`
- do not transmit raw prompt/completion by default
- store evidence: `Ledger_t` + `AuditCard_t`
- audit data must be replayable while minimizing leakage

---

## 3) Production Checklist (Must-Pass)
- GateVectorLen == 91 (hard assert)
- Fail-Closed never weakens (any failure → ΔΩ=0)
- CommitUnique is the only needle-eye
- AuditCard_t is always produced and replayable
- LSE requires Intent/Temporal/Physical all Complete
- ShadowOnly is used only under Fail-Closed (optional counter-measure)
- bypass paths are unconstitutional → Fail-Closed (Mother Law 6)

---

## 4) Minimal Evidence Closure (Do Not Break the Lock)

### 4.1 Gate90: intent_audit_group (extensions allowed only here)
Required:
- `distillation_risk_score` (or generalized `intent_risk_score`)
- `extraction_pattern_flags` (extensible: `cross_model_probe`, `federated_aggregation`)
- `base_tau`

Recommended evidence fields (still not new gates):
- `device_chain_hash` (cross-device continuity)
- `tenant_id`, `model_fingerprint`
- `zk_low_intent_proof` (placeholder)

### 4.2 SeedContinuity
- `seed_continuity_ok` (mock in reference; production must use secure time/nonce/device chain)
- optional: `pi_seed_t`, `session_binding`, `device_chain_hash`

### 4.3 Gate91: physical_proof (mock placeholder allowed)
- `thermo_proof_ok`
- `attestation_ok`
- `entropy_clone_risk_code`

### 4.4 AuditCard_t (always required)
Must include:
- `i_90`, `i_91`, `lse_budget_ok`, `i_flow`
- `commit_unique`, `world_writeback`
- `out_level`, `reason_code`
- `evidence_keys` at minimum:
  - `req_hash`, `gate90_hash`, `gate91_hash`, `ledger_head_hash`

---

## 5) OutLevel Under Fail-Closed (Not a Gate)
- `Normal`: only when allowed
- `ShadowOnly`: fail output with low risk or decoy; record fingerprint in audit
- `SafeHold`: for world-writeback contexts; record evidence only, execute nothing

---

## 6) Six Killer Extensions (Evidence-Only)
1) adaptive thresholds → `intent_audit_group.tau_effective` (audited)
2) ShadowOnly decoy → `poison_tag` + `decoy_payload` logged and audited
3) cross-device continuity → `device_chain_hash` + SeedContinuity binding
4) multi-tenant isolation → `cross_model_probe` + `tenant_id` + `model_fingerprint`
5) audit export → stable AuditCard schema + replayable evidence keys
6) low-intent ZK (placeholder) → `zk_low_intent_proof` + `zk_verify_result` audited

---

## 7) Reference Boundary
This repository is mock/reference only. Production systems must replace:
- Gate90 heuristics with verified intent/temporal evidence
- Gate91 mocks with real attestation/secure time/anti-replay
- sealed evidence pipeline (ledger, export controls)

See `CONSTITUTION.md` for the extension boundary.

**Signature**: Liangfeng Hu | YFCore Technology Limited
