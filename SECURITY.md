# SECURITY｜Responsible Disclosure & Constitutional Boundary

**V∞ Constitutional AIOS Bus Reference Implementation**  
**13 Mother Laws × GateVectorLen=91 × LSE Meta-Axiom**

## Supported Versions
Only the latest commit on the `main` branch of this reference repository is supported.

## Reporting a Security Issue
- **Do NOT** open a public GitHub Issue.
- Email: **security@yfcore.tech** (Liangfeng Hu)
- Include:
  - Clear description
  - Affected component (reference mock logic / OpenAPI schemas / constitution semantics)
  - Minimal reproduction steps using **only** `reference-impl/python/demo.py`
  - Expected vs actual behavior
  - Which invariant (if any) is violated:
    - Fail-Closed
    - CommitUnique needle-eye
    - GateVectorLen=91
    - AuditCard replay consistency

We will acknowledge receipt within **48 hours** and provide a response within **7 days**.

## Out of Scope (Explicit Red Lines)
We will ignore or close without comment any request for:
- Production ZKP circuits, real π_thermo verification keys, real hardware attestation chains, or real π_seed generators.
- Any attempt to weaken Fail-Closed, bypass CommitUnique, or change GateVectorLen=91.
- Requests to “remove physical proof” or “make distillation easier”.
- Any proposal treating historical patches as causal parent (violates Mother Law 1 & 8).

## Threat Model (Reference Level)
This repo assumes adversaries may attempt:
- Model extraction/distillation (batch probing, structured sampling)
- Device-farm concurrency (temporal discontinuity)
- Physical-proof forgery (missing real work / fake attestation)
- Cross-tenant / cross-model probing
- Federated aggregation distillation

Security root is **physical decidability** (Gate91) + **causal continuity** (Gate90), not pure semantic filtering.

## Constitutional Invariants (Non-Negotiables)
Any deviation is unconstitutional:
1) **Fail-Closed**: any gate fails or LSE fails → ΔΩ=0 and CommitUnique=0  
2) **CommitUnique** is the only needle-eye for any world writeback (ΔΩ≠0)  
3) **GateVectorLen=91** permanently; no new gates  
4) **Holographic AuditCard** for every request  
5) **Replay Consistency**: same evidence keys under same Ledger view reproduce the same verdict

## Known Limitations (Reference Boundary)
- Proof fields are **mock placeholders** in this repo.
- ShadowOnly decoy/poison behavior is **semantic demonstration**, not a production countermeasure recipe.
- Production deployments must supply real attestation, secure time/nonce, anti-replay, and sealed evidence pipelines.

## Responsible Disclosure Template
- Title:
- Affected module:
- Violated invariant (if any):
- Reproduction steps (demo.py only):
- Expected result:
- Actual result:
- Risk assessment:
- Suggested fix:

Thank you for helping keep the V∞ Constitution secure and locked.

**Signature**: Liangfeng Hu | YFCore Technology Limited
