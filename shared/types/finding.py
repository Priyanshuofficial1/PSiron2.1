from enum import StrEnum
from pydantic import BaseModel, Field

class FindingStatus(StrEnum):
    CONFIRMED="CONFIRMED"
    POTENTIAL="POTENTIAL"
    NOT_VERIFIED="NOT_VERIFIED"
    REJECTED="REJECTED"
    INFORMATIONAL="INFORMATIONAL"

class Finding(BaseModel):
    id: str
    title: str
    category: str
    severity: str
    confidence: float = Field(ge=0, le=1)
    status: FindingStatus
    asset: str
    location: str | None = None
    source_tools: list[str] = []
    evidence: list[str] = []
    cwe: str | None = None
    owasp: str | None = None
    root_cause: str | None = None
    impact: str | None = None
    remediation: str | None = None
