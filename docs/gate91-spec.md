# Gate91 Spec｜I_ENTROPY_CLONE (Physical Decidability Gate)

## Purpose
Gate91 rejects requests that lack credible **physical work / attestation evidence**.
In production this would bind to TEE attestation, secure timing, and anti-replay.

This reference repo provides the **interface shape** and **reason codes**.

## Inputs (Evidence)
`physical_proof` object:
- `thermo_proof_ok` (mock placeholder)
- `attestation_ok` (mock placeholder)
- `entropy_clone_risk_code` (string reason)
Optional evidence fields (still evidence-only):
- `attestation_report_hash`
- `nonce`
- `device_fingerprint_hash`

## Output
- `i_91` ∈ {0, 1} (0 pass, 1 fail)
- `entropy_clone_risk_code` (stable reason code)

## Reason Codes (Reference)
- `OK`
- `THERMO_OR_ATTEST_FAIL`
- `REPLAY_SUSPECTED` (placeholder)
- `ATTEST_CHAIN_INVALID` (placeholder)

## Mapping to Constitution
Gate91 is the physical component of GateVectorLen=91.
It cannot be removed, bypassed, or replaced with a new gate.
