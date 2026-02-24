"""
LSE Meta-Axiom Reference (Meta Gate 0)

Reference-only completeness and BudgetOK checks.
No production secure-time, anti-replay, or attestation chain validation is included.
"""

import json
import hashlib
from dataclasses import dataclass, asdict
from typing import Dict, Any, List


def _sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


@dataclass
class LedgerEvent:
    req_id: str
    event: str
    data: Dict[str, Any]


class InMemoryLedger:
    def __init__(self) -> None:
        self.events: List[LedgerEvent] = []

    def append(self, e: LedgerEvent) -> None:
        self.events.append(e)

    def historical_risk_index(self) -> float:
        if not self.events:
            return 0.0
        suspicious = sum(1 for e in self.events if e.event in ("FAIL_CLOSED", "DISTILL_ALERT", "THERMO_FORGERY"))
        return suspicious / max(1, len(self.events))

    def head_hash(self) -> str:
        tail = [asdict(e) for e in self.events[-10:]]
        return _sha(json.dumps(tail, sort_keys=True))


@dataclass
class LseVerdict:
    i_lse: str  # "0" or "+inf"
    budget_ok: bool
    complete_intent: bool
    complete_temporal: bool
    complete_physical: bool
    reason_code: str


def budget_ok(ledger: InMemoryLedger) -> bool:
    # Reference heuristic: budget fails if failures dominate.
    return ledger.historical_risk_index() < 0.60


def complete(intent_ok: bool, temporal_ok: bool, physical_ok: bool) -> bool:
    return bool(intent_ok) and bool(temporal_ok) and bool(physical_ok)


def evaluate_lse(ledger: InMemoryLedger, intent_ok: bool, temporal_ok: bool, physical_ok: bool) -> LseVerdict:
    b_ok = budget_ok(ledger)
    c_int = bool(intent_ok)
    c_tmp = bool(temporal_ok)
    c_phy = bool(physical_ok)
    all_ok = b_ok and complete(c_int, c_tmp, c_phy)

    if all_ok:
        return LseVerdict("0", True, c_int, c_tmp, c_phy, "PASS")

    if not b_ok:
        return LseVerdict("+inf", False, c_int, c_tmp, c_phy, "RC_LSE_BUDGET_FAIL")

    return LseVerdict("+inf", True, c_int, c_tmp, c_phy, "RC_LSE_INCOMPLETE")
