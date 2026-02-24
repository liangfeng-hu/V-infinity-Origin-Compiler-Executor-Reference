# Threat Model & Solution Mapping (Reference)

| Threat | Observable Evidence | Gate | Outcome | Reason Code |
|---|---|---|---|---|
| Batch extraction | high distillation_risk_score | Gate90 | Fail-Closed + ShadowOnly | RC_INTENT_OR_SEED_FAIL |
| Device farm | broken SeedContinuity / missing device_chain_hash | Gate90 | Fail-Closed | RC_INTENT_OR_SEED_FAIL |
| Fake physical proof | thermo/attest fail | Gate91 | Fail-Closed + ShadowOnly decoy | RC_THERMO_FORGERY |
| Cross-model probing | cross_model_probe flag | Gate90 | Fail-Closed | RC_INTENT_OR_SEED_FAIL |
| Slow penetration | rising Ledger risk index | LSE BudgetOK | tighten tau_effective | RC_LSE_BUDGET_FAIL |

## Reason Code Policy
Reason codes must be:
- stable
- auditable
- replayable

No additional gates are introduced by reason codes.
