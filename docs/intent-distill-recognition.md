# Intent Distillation Recognition (Reference)

## Purpose
Gate90 evaluates extraction risk through an evidence bundle (intent_audit_group).
This document defines reference-level signals (no exploit details).

## Evidence Fields (Examples)
- `distillation_risk_score` (0..1)
- `extraction_pattern_flags`:
  - `batch_probe`
  - `template_sweep`
  - `cross_model_probe`
  - `federated_aggregation`
- `historical_risk_index` (from Ledger)
- `device_chain_hash` (continuity)
- `request_rate_bucket` (coarse)

## Decision Sketch (Reference)
- risk_score < tau_effective
- seed continuity must pass
- critical flags (cross_model_probe, federated_aggregation) may hard-fail

All decisions must be recorded in AuditCard with replayable evidence keys.
