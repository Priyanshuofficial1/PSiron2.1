from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="PSiron2.1 Control Plane", version="0.1.0")

class AssessmentCreate(BaseModel):
    name: str
    authorization_ref: str
    safe_mode: bool = True

class TargetCreate(BaseModel):
    kind: str
    value: str

@app.get("/health")
def health():
    return {"status": "ok", "project": "PSiron2.1", "ai_runtime": False}

@app.post("/v1/assessments")
def create_assessment(payload: AssessmentCreate):
    return {"id": "pending", "status": "created", "authorization_ref": payload.authorization_ref, "safe_mode": payload.safe_mode}

@app.post("/v1/targets")
def create_target(payload: TargetCreate):
    return {"id": "pending", "kind": payload.kind, "value": payload.value}
