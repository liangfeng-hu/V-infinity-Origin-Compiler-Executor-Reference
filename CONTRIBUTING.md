# CONTRIBUTING｜How to Contribute (V∞ Reference)

This repository is a **sealed constitutional reference**. Contributions are welcome **only** if they preserve the lock.

## Read First
- `CONSTITUTION.md`
- `SECURITY.md`
- `docs/integration-guide.md`

## Allowed Contributions
1) **Documentation**
- Clarity, structure, terminology consistency
- More examples of integration and audit fields
- Threat model explanations (no actionable exploit scripts)

2) **OpenAPI / Spec**
- Schema comments, examples, version tags
- Consistent naming and payload shapes

3) **Reference Implementation**
Only within these boundaries:
- Add **evidence fields** ONLY inside:
  - `Gate90.intent_audit_group`, or
  - `AuditCard_t`
- Add demo scenarios showing:
  - Fail-Closed
  - ShadowOnly / SafeHold
  - AuditCard replayable evidence keys
- Refactoring: readability, type hints, comments
  - Must not change sealed semantics

## Absolute Red Lines (PR will be closed)
- Adding any new gate (GateVectorLen must remain 91)
- Weakening Fail-Closed semantics
- Bypassing CommitUnique for any world writeback
- Adding production ZKP/attestation/π_seed implementations or operational keys
- Providing executable attack scripts or bypass details
- Making distillation easier / removing physical proof
- Treating historical patches as causal parent (violates Mother Law 1 & 8)

## PR Checklist
- [ ] GateVectorLen remains 91
- [ ] Fail-Closed still forces ΔΩ=0 and CommitUnique=0 on any failure
- [ ] CommitUnique remains the only needle-eye for ΔΩ≠0
- [ ] Any new fields are only evidence fields inside intent_audit_group or AuditCard
- [ ] `python reference-impl/python/demo.py` runs
- [ ] Docs updated if schemas/fields changed
- [ ] No exploit/bypass details are added

## Contact
Security issues: see `SECURITY.md` (security@yfcore.tech)

**Signature**: Liangfeng Hu | YFCore Technology Limited
