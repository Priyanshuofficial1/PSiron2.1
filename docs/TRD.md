# PSiron2.1 Technical Requirements Document

## Architecture
Next.js/React/TypeScript client -> FastAPI control plane -> PostgreSQL metadata and Redis job state -> Docker worker pool -> immutable object evidence store. The MVP stays modular and avoids premature distributed complexity.

## Component boundaries
Web is presentation. API owns authentication, authorization, assessment state and orchestration requests. Engine owns planning, normalization, correlation and verification. Workers execute tool adapters. Evidence owns provenance and hashing. Graph owns relationships. Reporting consumes persisted models.

## Core data model
User, Project, Assessment, Target, Asset, Tool, ToolRun, Finding, Evidence, Verification, AttackPath, Remediation, Regression and Report. Assessment owns authorization and scope. Findings reference assets and evidence. ToolRuns preserve versions, configuration and raw output.

## API
GET /health
POST /v1/assessments
POST /v1/targets
Planned resources: assessments/{id}, scope, assets, tool-runs, findings, evidence, verifications, attack-paths, remediation, regressions and reports.

## Job architecture
Planner emits deterministic capability jobs. Scheduler assigns compatible workers. States: QUEUED, RUNNING, SUCCEEDED, FAILED, CANCELLED and BLOCKED. Stable job identifiers and idempotency keys prevent duplicate execution.

## Worker isolation
Workers run with CPU, memory, PID, filesystem, network and timeout limits. They receive only the scoped job envelope and required artifacts. Raw output is written to evidence storage with provenance.

## Tool registry
A ToolManifest records identity, repository, version/commit, license, capabilities, inputs, outputs, adapter, parser, evidence mapping, resource limits, timeout, prerequisites and safety policy. Repository onboarding reviews license, dependencies, capability and execution requirements before isolation.

## Normalization
Adapters parse native formats into stable shared models. Parser failure is visible as a tool-run failure and never creates invented findings.

## Correlation
Canonical keys use asset identity, location, vulnerability class, evidence fingerprints and provenance. Duplicates are merged while retaining source observations.

## Verification
Verification is scoped, policy-controlled and non-destructive by default. CONFIRMED requires successful verification plus evidence. Otherwise the status remains POTENTIAL, NOT_VERIFIED or REJECTED.

## Evidence
Evidence has type, SHA-256, timestamps, assessment/tool-run/verification references, storage location, redaction state and access metadata. Immutable storage is preferred.

## Graph
Asset graph contains discovered entities. Attack graph contains evidence-supported relationships. Every confirmed edge references evidence.

## Risk
No arbitrary security score. Store severity, exploitability, exposure, authentication, privilege, asset criticality, observed impact, potential impact and chain position separately.

## Security
Authentication and RBAC protect control-plane actions. Authorization and allowlists gate active tests. Secrets use environment or secret storage and are excluded from logs. Workers use least privilege and network policy.

## Limits
Per-job timeout, request rate, concurrency, CPU, memory, PID, artifact size and global scheduler quotas.

## Failure handling
Transient infrastructure failures may retry with bounded backoff. Tool and parser failures are visible terminal states. Verification must not silently mutate evidence semantics through uncontrolled retries.

## Idempotency
Assessment creation, job scheduling, evidence ingestion and report generation use stable identifiers and idempotency keys.

## Observability
Structured audit logs, job logs, health endpoints, metrics and trace identifiers. Credentials and unredacted secrets are excluded.

## Deployment
Docker Compose for local MVP. API, scheduler, workers and storage can later be separated without changing domain models.

## Testing
Unit, integration, E2E, adapter contract, verification and regression tests. Fixtures must use explicit evidence; production paths never manufacture findings.

## Performance
Stream large evidence to object storage. Bound parser memory and artifact size. Scale worker concurrency only within configured limits.

## Extensibility
New tool = manifest + adapter + parser + capability mapping + tests. New target type = ingestion schema + profiler + planner rules + applicable tools.

## Threat model
Threats include unauthorized scanning, SSRF, malicious artifacts, worker escape, secret leakage, evidence tampering, resource exhaustion and tool supply-chain compromise. Controls include scope gates, sandboxing, network policy, validation, hashing, redaction, quotas, provenance and least privilege.
