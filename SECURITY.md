# SECURITY｜安全声明与负责任披露（V∞ Reference Implementation）

**V∞-Origin-Compiler-Executor-Reference**  
**本源编译执行器通用宪法（13母律）× GateVectorLen=91 × LSE元公理**  
Responsible Disclosure & Strict Constitutional Boundary

（封板声明）  
本仓库为宪法参考实现，仅用于展示 Fail-Closed 语义、证据闭包与接口形状。  
冻结条件：GateVectorLen=91 永久不变；不新增任何门；扩展仅允许进入 Gate90.intent_audit_group 或 AuditCard_t；Fail-Closed 永不弱化；CommitUnique 为唯一针眼。

---

## 1. Supported Versions
Only the latest commit on the `main` branch of this reference repository is supported.

---

## 2. Reporting a Security Issue
- **Do NOT** open a public GitHub Issue.
- Email: **security@yfcore.tech** (Liangfeng Hu)
- Please include:
  - Clear description
  - Affected component (reference mock logic / OpenAPI schemas / constitution semantics)
  - Minimal reproduction steps using **only** `reference-impl/python/demo.py`
  - Expected vs actual behavior
  - Whether any constitutional invariant is violated (Fail-Closed / CommitUnique / GateVectorLen=91 / AuditCard replay)

We will acknowledge receipt within **48 hours** and provide a response within **7 days**.

---

## 3. Scope (What this repo is / is not)

### 3.1 In Scope
This repository is intentionally limited to:
- Interface specifications (OpenAPI)
- Semantic definitions & Fail-Closed reference logic
- Constitution text (**CONSTITUTION.md**)
- Vision & Roadmap documents
- Minimal reproducible demo (`reference-impl/python/demo.py`)

### 3.2 Out of Scope (Explicit Constitutional Red Lines)
We will ignore or close without comment any request for:
- Production ZKP circuits, real π_thermo verification keys, hardware attestation chains, or π_seed generator implementation.
- Any attempt to weaken Fail-Closed semantics, bypass CommitUnique needle, or change GateVectorLen=91.
- Any request to “remove physical proof” or “make distillation easier.”
- Any proposal that treats historical patches as causal parent (violates Mother Law 1 & 8).

---

## 4. Threat Model (Reference-Level)
This repo assumes adversaries may attempt:
- Model distillation / extraction (batch probing, structured sampling)
- Device farm & concurrency attacks (temporal discontinuity)
- Physical-proof forgery (missing real work / fake attestation)
- Cross-tenant / cross-model probing
- Federated aggregation distillation

The security root is **physical decidability** (Gate91) and **causal continuity** (Gate90), not pure semantic filtering.

---

## 5. Security Invariants (Constitutional Non-Negotiables)
Any deviation is considered unconstitutional:
1) **Fail-Closed**: if any gate fails or LSE is not satisfied → ΔΩ_t=0 and CommitUnique=0.  
2) **CommitUnique** is the only needle-eye for any world writeback (ΔΩ_t≠0).  
3) **GateVectorLen=91** permanently; no new gates are allowed.  
4) **Holographic Audit**: every request must produce an AuditCard_t with replayable evidence keys.  
5) **Replay Consistency**: same evidence keys under same Ledger_t view must reproduce the same verdict.

---

## 6. Known Limitations (Reference Boundary)
- Proof fields such as `thermo_proof_ok`, `attestation_ok`, and `seed_continuity_ok` are **mock placeholders** in this reference repo.
- ShadowOnly decoy/poison behavior is a **semantic demonstration** of Fail-Closed output strategies, not a production countermeasure recipe.
- Production deployments must supply real hardware attestation, secure time/nonce, anti-replay, and sealed evidence pipelines.

---

## 7. Responsible Disclosure Template
Please include the following:
- Title:
- Affected module:
- Violated invariant (if any):
- Reproduction steps (demo.py only):
- Expected result:
- Actual result:
- Risk assessment:
- Suggested fix:

---

Thank you for helping keep the V∞ Constitution secure and locked.

（封板签名）  
胡良锋（Liangfeng Hu）｜YFCore Technology Limited
