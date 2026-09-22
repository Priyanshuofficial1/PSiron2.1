# PSiron2.1 Product Requirements Document

## Vision
PSiron2.1 is an evidence-driven security assessment platform that orchestrates specialized open-source security tools and transforms raw results into correlated, verified vulnerabilities, attack paths, remediation guidance, regression tests, coverage and reproducible reports.

## Problem
Security tools operate in silos. Scanner output is duplicated, weakly contextualized and disconnected from source, runtime, identity, dependencies, infrastructure and workflows. PSiron2.1 supplies the control plane and evidence model that connects those layers without AI or LLM runtime dependencies.

## Goals
Accept diverse authorized assessment inputs; validate scope; discover and profile assets; select capabilities deterministically; execute tools in isolated workers; normalize and correlate observations; verify with evidence; model attack paths; separate observed from potential impact; provide remediation, regression, coverage and HTML/PDF/JSON reporting.

## Non-goals
No autonomous destructive exploitation, unscoped internet scanning, AI/LLM runtime, universal security guarantee, or arbitrary proprietary scanner replacement.

## Personas
Security engineer, penetration tester, application security engineer, developer, security lead and auditor.

## Target types
URL/domain/IP, repository/source tree, application/package, OpenAPI, container/image, cloud/IaC, Kubernetes manifests, Android APK, firmware/binary and PCAP/network evidence.

## Modes
Passive analysis, safe discovery, controlled active testing, authenticated application testing, source analysis, artifact analysis and regression retesting.

## Lifecycle
Create -> authorize -> scope -> ingest -> discover -> profile -> plan -> schedule -> execute -> collect -> normalize -> correlate -> verify -> graph -> risk context -> remediate -> regress -> report.

## Functional requirements
FR-01 assessment creation and authorization reference.
FR-02 explicit target and scope allowlists.
FR-03 target/artifact ingestion with hashes.
FR-04 asset discovery and profiling.
FR-05 deterministic capability planner.
FR-06 tool registry and version provenance.
FR-07 isolated worker execution.
FR-08 raw result preservation.
FR-09 common finding model.
FR-10 evidence-backed verification.
FR-11 correlation and deduplication.
FR-12 asset and attack graphs.
FR-13 separate risk factors, not arbitrary aggregate scores.
FR-14 remediation tracking.
FR-15 regression tests tied to findings.
FR-16 tested/untested coverage.
FR-17 HTML/PDF/JSON reports.
FR-18 audit trail.

## Security and authorization
Active testing requires explicit authorization and exact scope. Scope is checked at scheduling and execution. Safe mode is default and destructive actions are denied. Rate, concurrency, CPU, memory, process and timeout limits are mandatory. Credentials are protected and logs are redacted.

## Finding lifecycle
Tool observation -> POTENTIAL or INFORMATIONAL -> verification hypothesis -> controlled verification -> CONFIRMED, NOT_VERIFIED or REJECTED. Confirmation requires sufficient evidence. A scanner suspicion alone never becomes confirmed.

## Evidence lifecycle
Capture -> metadata -> SHA-256 hash -> immutable storage -> linkage to assessment/tool run/finding/verification -> report. Evidence includes requests, responses, screenshots, traces, source locations, tool output, logs, PCAP/config snapshots, timestamps, auth context, Git commit, target snapshot and tool versions.

## Correlation
Correlate by asset, endpoint, source location, technology, request fingerprint, vulnerability class, CWE/OWASP mapping, dependency and identity context while preserving source provenance.

## Attack graph
Nodes represent assets, identities, services, findings and sensitive resources. Edges carry evidence references and state. Confirmed edges require evidence; potential relationships remain potential.

## Risk
Store severity, exploitability, exposure, authentication requirement, privilege requirement, asset criticality, verified impact and attack-chain position as separate factors. Observed impact and potential impact are separate.

## Coverage
Report tested and untested domains, ports, endpoints, source files, dependencies, images, Kubernetes and cloud resources. Not tested is never secure.

## Web and vibe-code security
The dedicated web module covers framework detection, insecure patterns, authentication, APIs, client-side behavior, dependency analysis, runtime testing and verification for React, Next.js, Vite, Vue, Angular, Svelte, Node.js, Express, NestJS, Django, FastAPI, Flask, Spring, Rails and Go web applications. It targets secrets, XSS, insecure storage, authorization flaws, exposed endpoints, source maps, injection, SSRF, traversal, prototype pollution, deserialization, mass assignment, file upload, BOLA/IDOR, account takeover paths, data exposure, rate limits, GraphQL authorization, business logic and race conditions.

## Tool ecosystem
Recon: Nmap, Naabu, Amass, Subfinder, dnsx, httpx, Katana.
Web: ZAP, Nuclei, ffuf, Playwright, Katana.
API: ZAP, Schemathesis, Nuclei, Playwright.
Source: CodeQL, Semgrep, Gitleaks.
Supply chain: Trivy, Syft, Grype, OSV-Scanner.
Containers: Trivy, Syft, Hadolint, Dockle.
Cloud/IaC: Prowler, ScoutSuite, Checkov.
Kubernetes: Kubescape, kube-bench, Trivy.
Mobile: MobSF, JADX, Apktool, Frida.
AD: BloodHound CE, NetExec, Impacket, Certipy.
Network: TShark/Wireshark, Scapy, Nmap, testssl.sh.
Controlled validation: Metasploit, sqlmap, Impacket, NetExec behind policy gates.
Fuzzing: AFL++, libFuzzer, boofuzz, Schemathesis.
Binary: Ghidra, angr, Rizin, pwntools.
Firmware: Binwalk, FirmAE, Ghidra, QEMU.
Wireless: Aircrack-ng, Kismet, Bettercap, Scapy.

## UX
Professional cybersecurity cockpit with assessment progress, live jobs, assets, findings, evidence, attack graph, coverage, remediation, regression and reports. Every control maps to a real backend operation.

## Acceptance criteria
A scoped URL can be ingested, validated, assessed by available MVP tools, produce real tool runs, preserve raw output, normalize observations, attach evidence, verify selected findings, show coverage and export an HTML report. Tool failures and unsupported capabilities remain visible.

## MVP
Foundation, web assessment, source and dependency analysis.

## Post-MVP
API workflows, containers, cloud, Kubernetes, mobile, AD, fuzzing, binary, firmware, network and wireless.

## Milestones
M1 foundation; M2 web pipeline; M3 source/dependency; M4 API; M5 advanced modules; M6 hardening and reproducibility.

## Risks and limitations
Tool drift, false positives, target instability, expired authentication, resource exhaustion, incomplete coverage, parser defects and evidence leakage require provenance, isolation, limits, retries, redaction and explicit states. Passing a scan does not imply security.
