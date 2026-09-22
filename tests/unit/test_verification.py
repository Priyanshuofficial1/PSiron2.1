from engine.verification.decision import decide

def test_confirmation_requires_evidence():
    assert decide(verified=True, evidence_ids=[], reason="proof").status == "NOT_VERIFIED"

def test_verified_with_evidence_is_confirmed():
    assert decide(verified=True, evidence_ids=["ev-1"], reason="proof").status == "CONFIRMED"
