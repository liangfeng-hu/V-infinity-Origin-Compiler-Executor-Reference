# CONSTITUTION｜V∞ Origin Compiler-Executor Constitution (Reference)

**V∞ Constitutional AIOS Bus Reference Implementation**  
**13 Mother Laws × GateVectorLen=91 × LSE Meta-Axiom**  
**(Fail-Closed, CommitUnique Needle-Eye, Holographic AuditCard)**

(Sealed Statement)  
This file is the **canonical constitutional text** for the repository. It defines the **sealed semantics** and **non-negotiable invariants** of the V∞ bus reference implementation.

**Sealed Constraints (Do Not Break the Lock):**
1) **GateVectorLen ≡ 91** permanently; **no new gates** are allowed.  
2) Gate90 is the intent/causal/temporal “Awake Score” gate; Gate91 is the physical/entropy “Clone Resistance” gate.  
3) **LSE Meta-Axiom** (Meta Gate 0) requires **Intent × Temporal × Physical** to be simultaneously **Complete**.  
4) **Fail-Closed never weakens**: any failure → **ΔΩₜ=0** and **CommitUnique=0**.  
5) **CommitUnique** is the **only needle-eye** for any world writeback (**ΔΩₜ≠0**).  
6) Extensions may only add **evidence fields** inside:
   - `Gate90.intent_audit_group`, or
   - `AuditCard_t`
   (No new gates. No bypass. No hidden channels.)

**Reference Boundary:**  
This repository does **not** include production ZKP circuits, real attestation chains, real π_seed generators, or operational keys. It is a semantics + interface + audit closure reference.

---

## 0) Core Objects and World Effect

### 0.1 World Effect Variable
Define **world writeback** at time *t* as:
- **ΔΩₜ ≠ 0**: the system causes an externally observable effect.
- **ΔΩₜ = 0**: the system produces output and/or evidence only, without changing the world state.

### 0.2 Ledger and Audit Objects
- **Ledgerₜ**: append-only fact ledger (replayable, reproducible).
- **AuditCardₜ**: holographic audit closure for each request/response.
- **SeedContinuity**: temporal + device continuity evidence bundle (includes π_seedₜ and chain bindings).

### 0.3 Needle-Eye and Safe Semantics
- **CommitUnique=1** opens the **only** legal path that allows **ΔΩₜ≠0**.
- If any gate fails or LSE fails, the system must **Fail-Closed**:
  - ΔΩₜ = 0
  - CommitUnique = 0
  - Only evidence writes are allowed (Ledgerₜ, AuditCardₜ).

---

## 1) LSE Meta-Axiom (Meta Gate 0)

### 1.1 Purpose
LSE fuses the system’s decision into a **product closure**:
- Intent completeness
- Temporal (seed) continuity
- Physical decidability

If any dimension is incomplete, the whole decision must collapse to Fail-Closed.

### 1.2 Formal Definition (Reference)
Let:
- **Complete(Intent)**,
- **Complete(Temporal)**,
- **Complete(Physical)**  
be evidence completeness predicates.

Define:
- **I_LSE(Γₜ) = 0**  iff  Complete(Intent) ∧ Complete(Temporal) ∧ Complete(Physical)
- otherwise **I_LSE(Γₜ) = +∞**

### 1.3 BudgetOK (Entropy Watchdog Hook)
LSE includes a top-level constraint **BudgetOK**, derived from Ledger history and current evidence, used to defend against slow penetration and “long-horizon extraction” patterns.  
BudgetOK must be:
- computable from Ledgerₜ view,
- recorded into AuditCardₜ,
- replayable.

---

## 2) GateVectorLen = 91 (Sealed Gate Vector)

### 2.1 Gate Vector Definition
Let:
GateVector = (Gate1, Gate2, …, Gate89, Gate90, Gate91)

Where:
- **Gate90 = I_AWAKE_SCORE** (intent/causal/temporal gate)
- **Gate91 = I_ENTROPY_CLONE** (physical/entropy/attestation gate)

The dimension is sealed:
- **GateVectorLen ≡ 91** permanently.

### 2.2 Bus Verdict (I_FLOW)
Define **I_FLOW** as the bus verdict.

**I_FLOW = 0** iff:
- I_LSE = 0
- I_90 = 0
- I_91 = 0
- CommitUnique = 1

Otherwise:
- **I_FLOW = +∞**, and the system enters **Fail-Closed** semantics.

---

## 3) Gate90｜I_AWAKE_SCORE (Intent/Causality/Temporal Gate)

### 3.1 Purpose
Gate90 evaluates whether a request is causally consistent with legitimate usage and whether extraction intent is present, using:
- intent audit evidence
- seed continuity evidence
- ledger-derived historical risk

### 3.2 Inputs (Sealed Entry Points)
Gate90 may only read from these existing objects (fields can be expanded only as evidence):
1) **intent_audit_group** (the only allowed expansion surface for Gate90 evidence fields)
2) **SeedContinuity** (π_seedₜ and continuity bindings)
3) **Ledgerₜ** historical statistics (for adaptive thresholds)
4) **LSE BudgetOK** constraint

### 3.3 Outputs
Gate90 must output:
- **I_90 ∈ {0, +∞}** (or equivalent Pass/Fail encoding)

And must record into **AuditCardₜ** at minimum:
- intent_risk_score (or distillation_risk_score)
- τ_intent_effective (effective threshold, may adapt)
- extraction_pattern_flags (extensible only as evidence)
- seed_continuity_ok
- decision_reason_code (stable, replayable)

### 3.4 Allowed Extensions (Only Evidence Fields)
Gate90.intent_audit_group is the **only legal surface** for adding new Gate90 evidence fields, and all additions must satisfy:
1) No new gates are introduced.
2) Fields are purely evidence, not hidden control channels.
3) Fields are written to AuditCardₜ for holographic closure.
4) Fields remain replayable under Ledgerₜ view.

Recommended evidence-only fields (examples):
- device_chain_hash (cross-device continuity)
- cross_model_probe flag
- federated_aggregation flag
- historical_risk_index
- request_rate_bucket (coarse)
- zk_low_intent_proof (placeholder interface)

---

## 4) Gate91｜I_ENTROPY_CLONE (Physical/Entropy/Attestation Gate)

### 4.1 Purpose
Gate91 rejects requests that lack credible **physical work** evidence and device attestation.  
In production this binds to secure attestation + anti-replay + secure timing.  
In this reference repository it is expressed as interface shape + reason codes.

### 4.2 Inputs
Gate91 reads evidence fields such as:
- π_thermo (physical work/entropy proof placeholder)
- device attestation (placeholder)
- time/nonce bindings (placeholder)
All must be auditable and replay-referencable (as hashes/keys) in AuditCardₜ.

### 4.3 Outputs
Gate91 must output:
- **I_91 ∈ {0, +∞}** (or equivalent Pass/Fail encoding)
- entropy_clone_risk_code (stable reason code)

And must record into AuditCardₜ:
- thermo_proof_ok (reference placeholder)
- attestation_ok (reference placeholder)
- entropy_clone_risk_code

---

## 5) Fail-Closed Semantics

### 5.1 Definition
Fail-Closed means:
- ΔΩₜ = 0
- CommitUnique = 0
- Only evidence is written (Ledgerₜ and AuditCardₜ)
- Output may be downgraded (ShadowOnly) or held (SafeHold) depending on context

### 5.2 OutLevel (Not a Gate)
OutLevel is an output policy under Fail-Closed. It is **not** a new gate.
- **Normal**: only under I_FLOW=0
- **ShadowOnly**: return low-risk output/decoy; record fingerprints into AuditCardₜ
- **SafeHold**: for world-writeback contexts; record evidence only, execute nothing

---

## 6) AuditCardₜ (Holographic Self-Audit)

### 6.1 Required Fields (Minimum)
Every request must produce an AuditCardₜ containing at least:
- gatevector_len (=91)
- lse_budget_ok
- i_90, i_91
- i_flow
- commit_unique
- world_writeback (ΔΩ permission bit)
- out_level
- reason_code
- evidence_keys (replay keys)

Minimum evidence_keys include:
- req_hash
- gate90_hash
- gate91_hash
- ledger_head_hash

### 6.2 Replay Consistency Requirement
Given:
- identical evidence_keys, and
- the same Ledgerₜ view  
the system must reproduce the same verdict.  
Replay inconsistency is unconstitutional.

---

## 7) Reason Codes (Stable, Auditable, Replayable)

Reason codes are not gates. They are stable explanations bound to evidence.

Reference reason codes (minimum set):
- PASS
- RC_LSE_BUDGET_FAIL
- RC_LSE_INCOMPLETE
- RC_INTENT_OR_SEED_FAIL
- RC_THERMO_FORGERY

Rules:
1) Reason codes must be deterministic from evidence.
2) Reason codes must be recorded into AuditCardₜ.
3) Reason codes must not leak sensitive raw data by default (Mother Law 9).

---

## 8) The 13 Mother Laws (Constitutional Mother Layer)

**Note:** These laws constrain LSE, Gate90, Gate91, I_FLOW, and audit closure. They do not introduce new gates. They define invariants and obligations.

### Mother Law 1 — Origin Recompile
Implₜ = C(O, SSOT, Ledgerₜ).  
Any implementation must be derivable from invariants O, single source of truth SSOT, and Ledgerₜ.

### Mother Law 2 — Single Cost Function
The cost function must be single and auditable; no hidden parallel objectives may influence verdicts.

### Mother Law 3 — Zero-Loss Switch
Any version/model/policy switch requires ZLS_OKₜ; otherwise the system enters SafeHold (evidence only).

### Mother Law 4 — Evidence First
No evidence → no action. Insufficient evidence forces Fail-Closed.

### Mother Law 5 — Unique Needle-Eye
CommitUnique is the only lawful path enabling ΔΩₜ≠0. Any bypass is unconstitutional.

### Mother Law 6 — No Bypass Paths
Any path that circumvents Gate90/Gate91/LSE is illegal and must Fail-Close.

### Mother Law 7 — Output Sealing
OutFPₜ must be replayable and consistent with evidence closure; inconsistency forces Fail-Closed.

### Mother Law 8 — Causal Closure
Every verdict must be causally closed in Ledgerₜ. If closure cannot be formed → unconstitutional → Fail-Closed.

### Mother Law 9 — Minimal Leakage
Default to minimal disclosure. Under Fail-Closed, use ShadowOnly/SafeHold policies as needed, and avoid leaking raw sensitive data.

### Mother Law 10 — Holographic Self-Audit
Every request produces an AuditCardₜ containing replayable evidence keys and verdict closure.

### Mother Law 11 — Append-Only Ledger
Ledgerₜ is append-only. Any modification requires Zero-Loss Switch discipline.

### Mother Law 12 — Replay Equivalence
Under the same Ledger view and evidence keys, the verdict must be reproducible.

### Mother Law 13 — Entropy Watchdog
Under adversarial pressure, thresholds must be able to tighten based on ledger-derived risk history. Any relaxation requires auditable evidence and budget justification.

---

## 9) Sealing Clause (Final)
This constitution is sealed for the reference repository.  
All extensions must remain within evidence-only surfaces; no new gates; no weakening Fail-Closed; no bypass of CommitUnique.

**Signature**: Liangfeng Hu (胡良锋)  
**Entity**: YFCore Technology Limited  
**Sealed time**: 2026-02-24  
**Final statement**: V∞ is sealed; never break the lock.
