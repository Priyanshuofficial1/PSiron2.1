# Threat Model
Trust boundaries are browser/API, API/scheduler, scheduler/worker, worker/target and worker/evidence store. Threats: SSRF, malicious artifacts, sandbox escape, credential leakage, evidence tampering, scope expansion and resource exhaustion. Controls: allowlists, policy gates, isolation, least privilege, quotas, hashing, redaction and audit trails.
