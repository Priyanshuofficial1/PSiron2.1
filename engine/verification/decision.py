from dataclasses import dataclass

@dataclass(frozen=True)
class VerificationDecision:
    status: str
    reason: str
    evidence_ids: tuple[str, ...]

def decide(*, verified: bool, evidence_ids: list[str], reason: str) -> VerificationDecision:
    if verified and evidence_ids:
        return VerificationDecision("CONFIRMED", reason, tuple(evidence_ids))
    if evidence_ids:
        return VerificationDecision("POTENTIAL", reason, tuple(evidence_ids))
    return VerificationDecision("NOT_VERIFIED", reason, ())
