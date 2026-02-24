# V-infinity-Origin-Compiler-Executor Reference (V∞ AIOS Bus)

**V∞ Constitutional AIOS Bus Reference Implementation**  
**13 Mother Laws × GateVectorLen=91 × LSE Meta-Axiom**  
**(Fail-Closed, CommitUnique Needle-Eye, Holographic AuditCard)**

This repository presents a **reference implementation** of a constitutional “bus” that binds **digital outcomes** to **physical causality**.

**Core claim (sealed semantics):**  
Any high-value output and any world writeback **ΔΩₜ ≠ 0** must be **anchored** to:
- **Gate90 (I_AWAKE_SCORE):** intent/causality/time continuity evidence
- **Gate91 (I_ENTROPY_CLONE):** physical work / entropy / device attestation evidence  
…and fused by the **LSE Meta-Axiom** (Intent × Temporal × Physical must be Complete).  
If not satisfied → **Fail-Closed**.

---

## Sealed Invariants (Non-Negotiables)

- **GateVectorLen ≡ 91** (no new gates)
  - **Gate90**: I_AWAKE_SCORE (intent/causal/temporal)
  - **Gate91**: I_ENTROPY_CLONE (physical/entropy/attestation)
- **LSE Meta-Axiom (Meta Gate 0):** Intent × Temporal × Physical must all be Complete
- **Fail-Closed never weakens** (any failure → ΔΩₜ=0 and CommitUnique=0)
- **CommitUnique is the only needle-eye** for any world writeback (ΔΩₜ≠0)
- Extensions may **only** add **evidence fields** inside:
  - `Gate90.intent_audit_group`, or
  - `AuditCard_t`
  (No new gates. No bypass.)

> Boundary: This repository intentionally does **NOT** include production ZKP circuits, real attestation chains, or real π_seed generators. It is built for semantics, interfaces, and audit closure demonstrations.

---

## Quick Start (30 seconds)

```bash
python reference-impl/python/demo.py

You will see 4 scenarios and a full AuditCard_t for each run with replayable evidence keys.

Repository Tour
Canonical Constitution

CONSTITUTION.md — the sealed constitutional text (Mother Laws + LSE + Gate90/91 + I_FLOW)

Strategic Docs

docs/vision-and-beyond.md — trillion-dollar extensions whitepaper

docs/extension-roadmap.md — 6 “killer” extensions (still no new gates)

docs/v-infinity-aios-blueprint.md — AIOS bus blueprint for CTO/CISO/board

Engineering Docs

docs/gate91-spec.md — Gate91 evidence contract & risk semantics

docs/lse-meta-axiom.md — the LSE formal closure & BudgetOK

docs/intent-distill-recognition.md — reference threat features for extraction risk

docs/threat-model-and-solution.md — threat table, defense mapping, reason codes

docs/integration-guide.md — 3 integration modes (sidecar / agent needle / gateway)

Interface Specs

spec/gate91.openapi.json

spec/lse.openapi.json

Reference Implementation (Python)

reference-impl/python/demo.py — minimal shock demo + optional ShadowOnly decoy

reference-impl/python/gate91_reference.py — Gate91 mock evaluator + schema helpers

reference-impl/python/lse_reference.py — LSE evaluator + BudgetOK mock + audit helpers

CI

.github/workflows/demo.yml — runs demo and sanity-checks invariants

Demo Scenarios (What you’re seeing)

A_OK — passes LSE + Gate90 + Gate91 → CommitUnique=1, ΔΩ=1 (allowed path)

B_DISTILL — high extraction risk → Fail-Closed + ShadowOnly output

C_THERMO_FORGERY — physical proof fails → Fail-Closed + ShadowOnly decoy evidence

D_DEVICE_HOP — device continuity breaks → Fail-Closed (anti device-farm)

Security

Please read SECURITY.md before filing issues.

Sovereign Signature

Liangfeng Hu (胡良锋)
YFCore Technology Limited
Sealed time: 2026-02-24
Final statement: V∞ is sealed; never break the lock.
