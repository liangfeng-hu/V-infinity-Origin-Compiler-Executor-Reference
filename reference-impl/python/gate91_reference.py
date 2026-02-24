"""
Gate91 Reference (I_ENTROPY_CLONE)

This is a reference-only evaluator that uses mock placeholders:
- thermo_proof_ok
- attestation_ok

No production attestation chains or ZKP verification keys are included.
"""

from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class Gate91Verdict:
    i_91: int
    thermo_proof_ok: bool
    attestation_ok: bool
    entropy_clone_risk_code: str


def evaluate_gate91(req_id: str, physical_proof: Dict[str, Any]) -> Gate91Verdict:
    thermo_ok = bool(physical_proof.get("thermo_proof_ok", False))
    attest_ok = bool(physical_proof.get("attestation_ok", False))

    if thermo_ok and attest_ok:
        return Gate91Verdict(
            i_91=0,
            thermo_proof_ok=True,
            attestation_ok=True,
            entropy_clone_risk_code="OK",
        )

    return Gate91Verdict(
        i_91=1,
        thermo_proof_ok=thermo_ok,
        attestation_ok=attest_ok,
        entropy_clone_risk_code=physical_proof.get("entropy_clone_risk_code", "THERMO_OR_ATTEST_FAIL"),
    )


def to_dict(v: Gate91Verdict) -> Dict[str, Any]:
    return asdict(v)
