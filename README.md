# NVIDIA AI-Q Enterprise Deep Research Platform
## Production-Oriented Multi-Agent Research Runtime


## Architecture

```text
RESEARCH GOAL
     |
Intent / Depth Router
     |
Research Planner
     |
Query Decomposer
     |
Typed Research DAG
     |
Supervisor
     |
+-------------+-------------------+---------------+
| Web Research| Enterprise Search | Data Analysis |
+-------------+-------------------+---------------+
     |                 |                  |
 Public Sources   Private Sources     SQL / cuDF
     +-----------------+------------------+
                       |
                  AI-Q Layer
                       |
                 Source Router
                       |
               Hybrid Retrieval
                       |
       +---------------+---------------+
       |               |               |
    Vector DB     Knowledge Graph   Lexical Search
       +---------------+---------------+
                       |
                 Evidence Graph
                       |
                 Research Agent
                       |
             Contradiction Detection
                       |
                 Citation Engine
                       |
                    Writer
                       |
                  Evaluator
                       |
          PASS / CRITIQUE / RERESEARCH
                       |
              Final Research Report
```

## Repository

```text
app/
  agents.py
  api.py
  budget.py
  citations.py
  compiler.py
  config.py
  contradictions.py
  db.py
  domain.py
  evaluator.py
  evidence_graph.py
  main.py
  model_router.py
  models.py
  planner.py
  report.py
  retrieval.py
  runtime.py
  security.py
  source_policy.py
examples/
tests/
docs/
```

## Quick Start

```bash
unzip nvidia-aiq-enterprise-deep-research-platform.zip
cd nvidia-aiq-enterprise-deep-research-platform
cp .env.example .env
docker compose build
docker compose up -d
docker compose ps
curl http://localhost:8000/health
```

Deep research:

```bash
curl -X POST http://localhost:8000/v1/research   -H 'x-api-key: change-me'   -H 'Content-Type: application/json'   --data-binary @examples/deep_research.json
```

Shallow research:

```bash
curl -X POST http://localhost:8000/v1/research   -H 'x-api-key: change-me'   -H 'Content-Type: application/json'   --data-binary @examples/shallow_research.json
```

Inspect model routes:

```bash
curl http://localhost:8000/v1/models/routes -H 'x-api-key: change-me'
```

Interactive docs:

```text
http://localhost:8000/docs
```

## Host Development

```bash
docker compose up -d postgres redis qdrant opensearch
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Change service hostnames in `.env` to `localhost`, then:

```bash
uvicorn app.main:app --reload
pytest -q
ruff check .
```

## Database Inspection

```bash
docker compose exec postgres psql -U postgres -d aiq
```

```sql
\dt
SELECT * FROM research_runs;
SELECT * FROM research_tasks;
SELECT * FROM evidence;
SELECT * FROM claims;
SELECT * FROM outbox;
SELECT * FROM audit;
```


## 1. Product Definition

AI-Q is best treated as a research control plane rather than a single RAG chain: classify intent, choose research depth, plan, retrieve, analyze, track evidence, detect conflicts, synthesize, cite, evaluate and iterate.

## 2. Architecture

Separate orchestration, retrieval, evidence, model routing, evaluation and governance. Each layer has a typed contract and independent scaling/failure policy.

## 3. Shallow vs Deep Research

Shallow mode is bounded tool-augmented research for quick cited answers. Deep mode decomposes the problem, fans out research tasks, aggregates evidence, critiques gaps and produces a report.

## 4. Intent Routing

Classify conversational, shallow and deep requests. Routing should consider complexity, required freshness, number of sources, enterprise sensitivity, latency and budget.

## 5. Clarification

Ambiguous high-impact questions transition to WAITING_INPUT. Do not silently invent scope, geography, time range, business unit or definitions.

## 6. Query Decomposition

Transform a broad question into independently researchable subquestions with dependencies, source preferences and success criteria.

## 7. Research DAG

Use a DAG for parallelizable evidence collection and deterministic dependency tracking. Persist plan versions when replanning.

## 8. Supervisor

The supervisor manages progress and budgets but cannot bypass retrieval authorization or citation requirements.

## 9. Web Research Agent

Search only approved providers, rank primary/authoritative sources, preserve URL/title/date/provenance and respect freshness requirements.

## 10. Enterprise Search Agent

Query only resources the principal is authorized to access. Retrieval authorization must happen before retrieval, not only after generation.

## 11. Data Analysis Agent

Use governed SQL or sandboxed Python/cuDF-style analysis for structured evidence. Preserve query/code, dataset version and generated artifacts.

## 12. Hybrid Retrieval

Combine lexical search, dense vector retrieval, metadata filters, reranking and optional graph traversal. Fuse scores rather than treating one retriever as universally optimal.

## 13. Vector Retrieval

Use tenant/ACL filters before similarity search. Persist embedding model/version and chunk provenance.

## 14. Knowledge Graph

Represent entities and relationships useful for multi-hop research. Graph edges are evidence-bearing facts, not model-created authority.

## 15. Lexical Search

Keyword/BM25-style retrieval remains valuable for identifiers, names, error codes and exact phrases.

## 16. Reranking

Rerank a bounded candidate set with a dedicated model or scoring policy; preserve pre/post ranking scores for evaluation.

## 17. Source Router

Select enterprise RAG, web, papers, SQL, graph or MCP sources based on task requirements and authorization.

## 18. Evidence Graph

Maintain claims, evidence nodes and SUPPORTED_BY/CONTRADICTS/DERIVED_FROM edges so report claims remain traceable.

## 19. Source Quality

Score authority, directness, freshness, relevance, independence and access scope. A high retrieval score is not equivalent to factual reliability.

## 20. Deduplication

Canonicalize URLs/doc IDs and use content hashes/similarity to prevent many copies of the same source from appearing as independent corroboration.

## 21. Contradiction Detection

Compare claims on the same entity/metric/time period. Surface disagreements and prefer direct, current, authoritative evidence where justified; otherwise preserve uncertainty.

## 22. Citation Engine

Every material factual claim should point to evidence IDs that resolve to immutable source metadata.

## 23. Citation Validation

Verify evidence exists, was authorized, supports the claim and has not been superseded or removed.

## 24. Iterative Research

Critique coverage, contradictions and unsupported claims, generate targeted follow-up tasks and stop when quality thresholds or budgets are reached.

## 25. Research Budgets

Bound loops, tasks, sources, model calls, tool calls, wall time, tokens and monetary cost. Budgets prevent runaway deep research.

## 26. Model Routing

Route intent/shallow work to fast models and planning/research/writing/critique to reasoning profiles. Allow self-hosted Nemotron and configurable frontier models based on compliance/cost/capability.

## 27. Model Gateway

Centralize provider credentials, allowlists, privacy policy, token accounting, retries, fallbacks and telemetry.

## 28. Structured Outputs

Planner, source router, critic and evaluator must emit schema-validated data before entering control flow.

## 29. Enterprise RAG

Ingest authorized documents with extraction, chunking, embeddings, metadata and ACLs. Retrieval must preserve document/page/chunk provenance.

## 30. Multimodal Retrieval

Extract tables, charts, page elements and OCR while preserving page coordinates and source lineage.

## 31. MCP

Use MCP as a governed source/tool boundary. Authenticate workloads, validate schemas, filter discovery and log every invocation.

## 32. SQL Research

Expose parameterized/read-only query capabilities through a policy gateway; never let a model receive unrestricted database credentials.

## 33. cuDF Analysis

For large tabular analysis, dispatch an approved sandbox skill that can use GPU acceleration when beneficial; validate results against data/schema expectations.

## 34. Sandboxed Code

Generated analysis code runs in job-scoped OpenShell-compatible or equivalent isolation with resource/network/filesystem controls.

## 35. Artifacts

Persist generated CSVs, charts, notebooks and reports in SQL/S3-compatible storage with hashes and lineage.

## 36. Job-Scoped State

Researchers share only the state needed for a research job. Do not use global mutable scratch state.

## 37. Durable Runtime

Persist run/task/attempt/evidence/report state and drive distributed work from a transactional outbox.

## 38. Transactional Outbox

Commit workflow state and dispatch intent atomically, then publish asynchronously to Kafka/Pulsar.

## 39. Worker Leases

Use expiring leases plus fencing tokens for distributed researcher workers.

## 40. Idempotency

Scope keys by tenant/run/task/action. Repeated dispatch must not duplicate expensive searches or external effects.

## 41. Retries

Retry transient failures with exponential backoff, jitter and global retry budgets.

## 42. Circuit Breakers

Stop amplification when a model, retriever or source is unhealthy.

## 43. Backpressure

Bound concurrent deep research, source fan-out, model calls, sandbox jobs and artifact bytes.

## 44. Cancellation

Cancellation is durable and propagated to workers/sandboxes/providers where supported.

## 45. Enterprise Identity

Represent human principal, tenant, workload, connector and source identities independently.

## 46. RBAC and ABAC

Use role plus attributes such as department, project, document classification, region and purpose.

## 47. Retrieval Authorization

Filter before search and before context assembly. Never retrieve a forbidden chunk and hope the generator will ignore it.

## 48. Secrets

Use workload identity or short-lived secret brokerage. Never place connector credentials in prompts or reports.

## 49. Prompt Injection

Enterprise documents and web pages are untrusted data; embedded instructions cannot grant tool access or change system policy.

## 50. Data Exfiltration

Enforce egress allowlists, DLP and model-provider policy before enterprise text leaves the trusted boundary.

## 51. Multi-Tenancy

Scope SQL, caches, queues, vector indexes, search, artifacts, traces and budgets by trusted tenant ID.

## 52. Privacy

Minimize retained prompts and retrieved text, classify artifacts and implement deletion/retention workflows.

## 53. Audit

Record query, principal, source authorization, model/tool versions, evidence IDs, report version and policy decisions.

## 54. Observability

Trace query -> router -> planner -> researcher -> source -> evidence -> writer -> evaluator. Track latency, cost and quality.

## 55. Quality Metrics

Measure citation coverage, source quality, answer completeness, contradiction handling, freshness and human acceptance.

## 56. Evaluation Harness

Maintain benchmark and organization-specific golden datasets. Evaluate shallow and deep workflows independently.

## 57. Freshness

Require explicit as-of timestamps for time-sensitive research and penalize stale evidence.

## 58. Research Reproducibility

Persist plan, source queries, evidence metadata, model/prompt versions and report hash.

## 59. Caching

Cache safe source results and embeddings with ACL-aware keys, TTLs and invalidation.

## 60. Failure Recovery

Resume from durable tasks/evidence rather than restarting a long research job from scratch.

## 61. Multi-Region

Route research to regions compatible with data residency and model/source availability.

## 62. Disaster Recovery

Restore SQL/artifact state, replay outbox, re-establish workers and resume only safe idempotent research tasks.

## 63. Capacity Planning

Model queries/day, tasks/query, sources/task, tokens/source, vector/search QPS, sandbox minutes and artifact volume.

## 64. Cost Governance

Attribute model, search, GPU, sandbox and storage costs per tenant/run and enforce hard/soft budgets.

## 65. Kubernetes

Separate API, planner, scheduler, researcher, writer, evaluator, connector and sandbox workloads.

## 66. Autoscaling

Scale on queue lag, oldest task, model/source latency and sandbox/GPU demand.

## 67. CI/CD

Run unit, contract, retrieval, security, eval, load and chaos suites before progressive deployment.

## 68. Contract Tests

Validate source/MCP/model schemas, authentication, timeout/error behavior and version compatibility.

## 69. Load Tests

Exercise large fan-out, slow sources, long reports and concurrent deep-research jobs.

## 70. Chaos Tests

Kill workers, duplicate messages, fail search/vector services and time out models; verify no lost or cross-tenant evidence.

## 71. Security Tests

Test ACL bypass, prompt injection, SSRF, source spoofing, citation substitution, secret leakage and sandbox escape.

## 72. Application: Competitive Intelligence

Combine authorized internal strategy with current public evidence; surface contradictions and date every market claim.

## 73. Application: Engineering Research

Research code/docs/incidents plus public technical material and produce an evidence-linked design report.

## 74. Application: Financial Research

Use approved internal data plus public filings/market sources with strict time-period and citation controls.

## 75. Application: Product Research

Combine feedback, support data, analytics and external market evidence to identify themes with traceable support.

## 76. Application: Incident Investigation

Correlate runbooks, logs, incident history and public dependency information while preserving source lineage.

## 77. Application: Scientific Research

Search papers, internal experiment data and structured analysis; preserve methods, datasets and conflicting findings.

## 78. Application: Executive Briefing

Deep-research a question, then generate a concise executive synthesis backed by drill-down evidence.

## 79. Code Walkthrough

domain.py defines research contracts; planner.py decomposes; compiler.py validates; retrieval.py collects; evidence_graph.py tracks provenance; contradictions.py finds conflicts; citations.py validates support; agents.py researches/critiques; model_router.py routes models; runtime.py coordinates; report.py writes; evaluator.py scores; models.py provides durable foundations.

## 80. Local Run Mode

The included mock source/model mode makes the architecture runnable without NVIDIA keys or private enterprise connectors.

## 81. Production Integration

Replace mock retrieval with deployment-owned NVIDIA RAG/LlamaIndex/OpenSearch/MCP/web/paper/SQL adapters and connect model routing to approved NIM/frontier endpoints.

## 82. Production Readiness

Add OIDC/workload identity, Alembic, persistent transitions, outbox publisher, Kafka/Pulsar, distributed workers, leases/fencing, persistent artifacts/evidence, OpenTelemetry, real source adapters and Kubernetes.

## 83. Principal-Level Design

The core distinction is between reasoning, evidence and authority: models propose; retrieval policy controls access; evidence supports claims; evaluators measure quality; the durable runtime owns execution truth.

## Research State Machines

```text
RUN:
CREATED -> CLASSIFYING -> PLANNING -> RESEARCHING
 -> SYNTHESIZING -> EVALUATING
 -> RERESEARCHING -> COMPLETED
 -> WAITING_INPUT / FAILED / CANCELLED

TASK:
PENDING -> READY -> RUNNING
 -> SUCCEEDED / FAILED / CANCELLED
```

## Evidence Model

```text
Claim
  |
  +-- SUPPORTED_BY --> Evidence
  +-- CONTRADICTED_BY -> Evidence
  +-- DERIVED_FROM --> Analysis Artifact

Evidence
  |
  +-- source URI / document ID
  +-- title
  +-- retrieved-at
  +-- authority
  +-- freshness
  +-- relevance
  +-- tenant/access scope
  +-- immutable content/artifact hash in production
```

## Production Research Loop

```text
PLAN
  -> RESEARCH
  -> BUILD EVIDENCE GRAPH
  -> SYNTHESIZE CLAIMS
  -> DETECT CONTRADICTIONS
  -> VALIDATE CITATIONS
  -> EVALUATE COVERAGE
       |
       +-- gaps + budget remains --> TARGETED RERESEARCH
       |
       +-- sufficient evidence --> WRITE REPORT
```

## Production Data Plane

```text
Enterprise Sources
  -> extraction/chunking
  -> ACL metadata
  -> embeddings
  -> vector index

Structured Data
  -> governed SQL gateway
  -> sandboxed analysis

Knowledge Graph
  -> authorized graph traversal

Web/Papers
  -> approved search providers

All paths
  -> normalized Evidence objects
  -> Evidence Graph
```

## Transactional Outbox

```sql
BEGIN;

UPDATE research_tasks
SET status='READY'
WHERE id=:task_id;

INSERT INTO outbox(event_type, aggregate_id, payload)
VALUES ('RESEARCH_TASK_READY', :task_id, :payload);

COMMIT;
```

## Exactly-Once Reality

```text
at-least-once dispatch
+ idempotent retrieval/task execution
+ immutable evidence IDs
+ leases/fencing
+ durable checkpoints
```

Research is primarily read-oriented, but duplicate expensive work still matters for cost and reproducibility.

## Model Routing Strategy

```text
Intent classification / shallow
  -> low-latency approved profile

Planning / research / critique / writing
  -> reasoning profile (for example self-hosted Nemotron)

Exceptional orchestration task
  -> approved frontier model when policy permits

Sensitive workload
  -> self-hosted/on-prem profile
```

The model router is policy-driven, not hard-coded to a single provider.

## Production Deployment

```text
API Gateway
    |
Research API
    |
Intent Router / Planner / Source Router
    |
Distributed SQL + Outbox
    |
Kafka / Pulsar
    |
+----------+-----------+----------+----------+
|Researcher|Retriever  |Analysis  |Writer    |
|Workers   |Workers    |Workers   |Workers   |
+----------+-----------+----------+----------+
    |
MCP / Enterprise RAG / Search / SQL / Graph
    |
Evidence + Artifact Storage
    |
Evaluator / Audit / OpenTelemetry
```

## Production Readiness Checklist

```text
[ ] OIDC + workload identity
[ ] RBAC/ABAC and retrieval ACL enforcement
[ ] persistent run/task/evidence/report transitions
[ ] Alembic migrations
[ ] transactional outbox publisher
[ ] Kafka/Pulsar
[ ] distributed researcher workers
[ ] leases/fencing/idempotency
[ ] approved web/paper search adapter
[ ] NVIDIA RAG or deployment-owned RAG adapter
[ ] vector ACL filtering
[ ] knowledge-graph adapter
[ ] governed SQL gateway
[ ] MCP gateway
[ ] OpenShell-compatible analysis sandbox
[ ] NIM/Nemotron model adapter
[ ] optional approved frontier-model adapter
[ ] persistent artifact storage
[ ] immutable evidence snapshots/hashes
[ ] citation support verification
[ ] organization-specific evaluation corpus
[ ] OpenTelemetry + dashboards + alerts
[ ] Kubernetes + autoscaling
[ ] load/chaos/security testing
[ ] retention/deletion/data-residency controls
[ ] backup and DR drills
```

## Troubleshooting

### 401
Ensure `x-api-key` matches `.env`.

### PostgreSQL connection failure
Use `postgres` inside Compose and `localhost` from host development.

### Qdrant/OpenSearch unavailable
The reference runtime's mock retriever does not require them for the example. Production hybrid retrieval adapters should fail explicitly or degrade according to policy.

### Research stops early
Check `MAX_RESEARCH_LOOPS`, `MAX_TASKS`, `MAX_SOURCES`, `MAX_MODEL_CALLS`, `MAX_TOOL_CALLS` and `MAX_BUDGET_USD`.

### No NVIDIA key
Local mode works without one. Real NIM/Nemotron integration requires an approved endpoint and credentials.

## Implementation Boundary

This code is a substantive, executable production-oriented reference architecture, not a claim that a generic ZIP can be dropped unchanged into an enterprise. Real production requires organization-specific identity, ACLs, data connectors, NVIDIA/model endpoints, web-search providers, retention rules, security controls, SLOs, evaluation data and infrastructure.

It intentionally does not invent private enterprise connectors, credentials or proprietary NVIDIA implementation details.

## Principal-Level Rule

```text
Model        -> proposes research actions and synthesis
Planner      -> decomposes the question
Compiler     -> validates the research DAG
Policy       -> controls source/model/tool authority
Retrievers   -> collect authorized evidence
Evidence Graph -> preserves provenance
Critic       -> finds gaps and contradictions
Citation Engine -> binds claims to evidence
Evaluator    -> measures quality
Budget       -> bounds autonomy
Durable Runtime -> owns execution truth
Audit        -> reconstructs the research process
```

**Deep research is not “RAG with more tokens.” It is a governed, budgeted, evidence-tracked iterative workflow.**



# Extended Professional Architecture & Operations Guide

## 1. NVIDIA AI-Q Blueprint Alignment

The public NVIDIA AI-Q Blueprint is a deployable research backend centered on intelligent query routing, shallow and deep research, pluggable knowledge retrieval, concurrent researcher workers, writer-led synthesis, skills, optional job-scoped sandbox execution, generated-file persistence, and evaluation. This repository mirrors those architectural responsibilities without claiming to reproduce NVIDIA proprietary internals.

The production mental model is:

```text
User / Application
       |
Authentication + Request Context
       |
Intent Classifier
  +----+------------------+
  |                       |
 Meta / Conversation   Research
                          |
                   Depth Decision
                    /          \
              Shallow          Deep
                 |               |
        Bounded Research     Clarifier
                 |               |
                 |         Source Router
                 |               |
                 |            Planner
                 |               |
                 |      Concurrent Researchers
                 |               |
                 |          Shared State
                 |               |
                 +-----------> Writer
                                 |
                        Citation Verification
                                 |
                              Report
```

## 2. Why This Is Multi-Agent Research, Not Ordinary RAG

Ordinary RAG commonly looks like:

```text
query -> retrieve top-k -> stuff context -> generate
```

A production research agent instead performs:

```text
understand question
 -> determine research depth
 -> clarify ambiguity
 -> choose authorized sources
 -> decompose question
 -> plan research
 -> dispatch focused researchers
 -> collect evidence
 -> analyze structured data
 -> construct evidence graph
 -> detect conflicts
 -> identify evidence gaps
 -> perform targeted re-research
 -> synthesize report
 -> validate citations
 -> evaluate quality
 -> preserve audit/replay data
```

The important architectural difference is that retrieval becomes one capability inside a larger durable reasoning workflow.

## 3. Intent Classifier

The intent classifier is the cheapest decision point in the system. It should determine:

```text
meta/conversational
research/shallow
research/deep
```

A production classifier considers question complexity, requested output form, freshness, source diversity, analytical requirements, expected latency and policy constraints.

It must emit structured output, for example:

```json
{
  "intent": "research",
  "depth": "deep",
  "reason": "requires multiple independent sources and synthesis"
}
```

The classifier routes work; it does not grant access to data sources.

## 4. Clarifier

Deep research should not silently invent important missing scope.

Potential clarification dimensions include:

```text
time period
geography
business unit
product/version
target audience
desired report format
internal vs external evidence
comparison criteria
required freshness
```

A durable production runtime can enter:

```text
WAITING_INPUT
```

and resume from the same checkpoint when the answer arrives.

## 5. Shallow Researcher

The shallow path optimizes latency and cost.

```text
question
 -> authorized tools
 -> bounded tool loop
 -> evidence
 -> cited synthesis
```

Typical controls:

```text
max LLM turns
max tool iterations
max sources
wall-clock timeout
token budget
cost budget
```

When the budget is exhausted, the researcher must synthesize from evidence already collected rather than continue indefinitely.

## 6. Deep Research Orchestrator

Deep research coordinates roles rather than attempting all work inside one prompt.

```text
DeepResearch
   |
   +-- source routing
   +-- structured planning
   +-- parallel research workers
   +-- evidence aggregation
   +-- critique
   +-- writer
   +-- citation verification
```

The orchestrator owns coordination but not source authorization.

## 7. Structured Research Planner

A research plan should be machine-readable.

Example:

```json
{
  "objective": "Assess enterprise GPU analytics migration",
  "queries": [
    {
      "id": "q1",
      "question": "What workloads currently dominate analytics compute?",
      "preferred_sources": ["enterprise_search"],
      "fallback_sources": [],
      "priority": 1
    },
    {
      "id": "q2",
      "question": "What current GPU acceleration approaches apply?",
      "preferred_sources": ["web_search", "papers"],
      "priority": 1
    }
  ]
}
```

The compiler validates task IDs, source names, dependencies, limits and authorization before execution.

## 8. Concurrent Researcher Workers

Independent queries should run concurrently when source quotas permit.

```text
Planner
  |
  +-- Research Query A -> Researcher Worker
  +-- Research Query B -> Researcher Worker
  +-- Research Query C -> Researcher Worker
  +-- Research Query D -> Researcher Worker
                         |
                    Evidence Merge
```

Concurrency must be bounded to protect search providers, model endpoints, databases and enterprise systems.

## 9. Shared Research State

Shared state should distinguish transient coordination from durable generated artifacts.

A research job can maintain:

```text
/shared/plan.json
/shared/progress.json
/shared/notes/
shared evidence references
writer outline
final report
```

Do not confuse this state with enterprise source data or global agent memory.

## 10. Source Router

The source router recommends sources from an already authorized set.

Correct:

```text
Identity/Policy -> Allowed Sources -> Source Router -> Preferred Order
```

Incorrect:

```text
LLM Source Router -> arbitrary source access
```

A router can consider data type, freshness, authority, cost, latency and task fit.

## 11. Data Source Registry

Maintain metadata for each source:

```text
source_id
type
owner
description
capabilities
authorization policy
regions
freshness
cost class
health
rate limits
tool binding
version
```

Per-request source filtering should be a hard security boundary.

## 12. Enterprise Knowledge Layer

The enterprise retrieval plane may use:

```text
NVIDIA RAG Blueprint
LlamaIndex
OpenSearch
Azure AI Search
vector databases
enterprise search
MCP tools
custom retrieval services
```

The agent should depend on a normalized evidence contract rather than vendor-specific payloads.

## 13. Ingestion Architecture

```text
Enterprise Documents
      |
Extraction
      |
Normalization
      |
Chunking
      |
Classification / ACL Metadata
      |
Embedding
      |
Vector Index
      |
Lexical Index
      |
Optional Entity Extraction
      |
Knowledge Graph
```

Store source document ID, page/section, version, ACL and content hash.

## 14. Hybrid Retrieval

A robust retrieval pipeline can combine:

```text
metadata filters
BM25 / lexical search
dense vector search
graph traversal
SQL lookup
reranking
```

One possible fusion model:

```text
score =
  w1 * lexical
+ w2 * dense
+ w3 * reranker
+ w4 * freshness
+ w5 * authority
```

Weights should be evaluated, not guessed permanently.

## 15. Retrieval Authorization

Authorization occurs before retrieval and before context assembly.

```text
principal
 -> tenant
 -> roles/attributes
 -> allowed corpus/documents
 -> retrieval filter
 -> candidate results
```

A forbidden document must not be retrieved and then merely hidden from the final answer.

## 16. Evidence Object

Every source result should normalize to something like:

```json
{
  "evidence_id": "ev_...",
  "source_type": "enterprise",
  "uri": "enterprise://...",
  "title": "...",
  "snippet": "...",
  "retrieved_at": "...",
  "authority": 0.9,
  "freshness": 0.8,
  "relevance": 0.92,
  "access_scope": "tenant/project",
  "metadata": {}
}
```

This creates a stable interface between retrieval and research reasoning.

## 17. Evidence Graph

The evidence graph provides traceability.

```text
Claim A
  +--SUPPORTED_BY--> Evidence 1
  +--SUPPORTED_BY--> Evidence 2

Claim B
  +--SUPPORTED_BY--> Evidence 3
  +--CONTRADICTED_BY--> Evidence 4

Evidence 3
  +--DERIVED_FROM--> Dataset X
```

The graph is useful for citations, contradiction analysis, auditing and report regeneration.

## 18. Evidence Independence

Ten syndicated copies of the same article are not ten independent sources.

Track:

```text
canonical source
publisher
upstream source
content hash
near-duplicate cluster
```

Source independence can affect confidence.

## 19. Contradiction Detection

Contradiction detection should align statements by:

```text
entity
metric
unit
time period
geography
definition
population
```

Many apparent contradictions are scope mismatches.

The system should surface unresolved disagreements rather than force false certainty.

## 20. Citation Engine

The writer should cite evidence IDs, not fabricate URLs.

```text
Writer
 -> claim
 -> evidence IDs
 -> deterministic resolver
 -> final citation
```

This separates natural-language synthesis from citation integrity.

## 21. Citation Verification

For every citation verify:

```text
evidence exists
source was actually retrieved
source was authorized
URI is allowed
claim has plausible support
source metadata is intact
```

Invalid citations should be removed or cause evaluation failure.

## 22. Writer Agent

The writer consumes:

```text
original question
clarifications
approved plan
research notes
evidence graph
contradictions
analysis artifacts
citation map
```

The writer should not freely perform hidden new research unless the workflow explicitly permits it.

## 23. Iterative Re-Research

A critic can identify:

```text
unsupported claims
missing subtopics
weak source authority
stale evidence
unresolved contradiction
insufficient quantitative evidence
```

Then create targeted tasks rather than restarting the whole job.

## 24. Stop Conditions

Deep research must stop.

Example:

```text
citation coverage >= threshold
AND required sections complete
AND no critical unsupported claims
AND unresolved contradiction count acceptable
OR research budget exhausted
```

Budget exhaustion should be reported as a limitation.

## 25. Research Budget Manager

Track:

```text
research loops
tasks
sources
model calls
tool calls
tokens
sandbox minutes
GPU minutes
wall time
monetary cost
```

Budgets can be enforced per run, tenant and source provider.

## 26. Model Routing

A production deployment can map roles to different models:

```text
intent classifier -> low latency
shallow researcher -> fast tool-capable model
planner -> reasoning model
research worker -> research/tool model
writer -> long-context synthesis model
critic -> reasoning/evaluation model
```

Self-hosted models may be selected for sensitive enterprise data.

## 27. NVIDIA NIM / Nemotron Integration Boundary

Keep inference behind a model gateway.

```text
Agent
 -> Model Gateway
 -> policy
 -> provider routing
 -> NIM / Nemotron / approved provider
```

The gateway handles credentials, timeouts, retries, model allowlists, token accounting and telemetry.

## 28. Frontier Model Integration

If an organization permits frontier models, route only approved workloads.

Policy may consider:

```text
data classification
tenant
region
task type
cost
context size
model capability
```

Do not send sensitive enterprise text to an external provider merely because it performs better on a benchmark.

## 29. MCP Integration

MCP provides a standard tool boundary.

```text
AI-Q Agent
  |
MCP Client/Gateway
  |
Policy + Identity
  |
MCP Servers
  |
Enterprise Systems
```

Filter tool discovery and validate arguments.

## 30. MCP Server Security

For each MCP invocation record:

```text
tenant
principal
run
task
server
tool
arguments hash
policy decision
deadline
result
trace
```

Tool descriptions are untrusted metadata and cannot grant permissions.

## 31. Data Analysis Agent

Structured research often requires more than retrieval.

Examples:

```text
SQL aggregation
CSV analysis
statistical comparison
trend calculation
table join
chart generation
cuDF acceleration
```

Generated code should execute in an isolated sandbox.

## 32. Job-Scoped Sandbox

One deep-research job can receive an isolated sandbox.

```text
Research Runtime
   |
Sandbox Gateway
   |
Job Sandbox
   +-- ephemeral filesystem
   +-- resource limits
   +-- network policy
   +-- approved packages
   +-- generated artifacts
```

Inference credentials and source credentials should remain outside untrusted code.

## 33. OpenShell-Compatible Execution

A production OpenShell-compatible integration should enforce policy outside the agent process.

Use cases include:

```text
Python analysis
CSV transformation
chart creation
notebook generation
data validation
```

## 34. Generated Files

Research may produce:

```text
report.md
report.pdf
chart.png
analysis.csv
notebook.ipynb
supporting JSON
```

Generated files should have durable IDs, content hashes, classification and lineage.

## 35. Artifact Storage

Recommended architecture:

```text
SQL metadata
  +
S3-compatible object storage
```

Store:

```text
artifact ID
run ID
creator step
MIME type
hash
size
classification
object key
created time
retention
```

## 36. Durable Research Runtime

The local implementation is synchronous for clarity. A production runtime should persist every meaningful transition.

```text
RUN
CREATED
 -> CLASSIFYING
 -> PLANNING
 -> RESEARCHING
 -> WRITING
 -> VERIFYING
 -> EVALUATING
 -> COMPLETED
```

Alternative states:

```text
WAITING_INPUT
RERESEARCHING
CANCEL_REQUESTED
FAILED
CANCELLED
```

## 37. Task Runtime

```text
PENDING
 -> READY
 -> RUNNING
 -> SUCCEEDED
```

Failure paths:

```text
RUNNING -> FAILED
RUNNING -> CANCELLED
RUNNING -> RETRY_WAIT
```

## 38. Transactional Outbox

Never update durable state and publish work as unrelated operations.

```sql
BEGIN;

UPDATE research_tasks
SET status='READY'
WHERE id=:id;

INSERT INTO outbox(event_type, aggregate_id, payload)
VALUES ('RESEARCH_TASK_READY', :id, :payload);

COMMIT;
```

A separate publisher sends the event to Kafka/Pulsar.

## 39. Kafka / Pulsar

Useful topics:

```text
research.task.ready
research.task.result
research.report.write
research.evaluate
research.audit
artifact.created
```

Partition by run ID when ordering within a research job matters.

## 40. Worker Leases

Distributed workers claim tasks with expiration.

```text
worker A owns task until T
```

If A dies, another worker can reclaim it after T.

## 41. Fencing

Every ownership transfer increments a fencing token.

A stale worker must not commit after a newer owner exists.

## 42. Idempotency

A safe key can be:

```text
tenant / run / task / attempt-semantic-version
```

Persist request hash and result.

## 43. Retry Policy

Retry:

```text
timeouts
429
temporary 5xx
connection resets
```

Do not blindly retry:

```text
authorization failures
invalid schemas
policy denial
permanent source errors
```

## 44. Circuit Breakers

If a source or model fails repeatedly:

```text
CLOSED -> OPEN -> HALF_OPEN -> CLOSED
```

Allow graceful degradation when policy permits.

## 45. Backpressure

Limit:

```text
active deep-research jobs
researchers per job
tool calls
source QPS
model concurrency
sandbox jobs
artifact bytes
```

## 46. Cancellation

Cancellation should persist before workers are signaled.

A cancelled research job must not continue spending model/search budget.

## 47. Checkpointing

Checkpoint after:

```text
classification
clarification
plan creation
research batch
evidence merge
writer output
citation verification
evaluation
```

This supports resume and replay.

## 48. Conversation State vs Research State

Conversation state contains interaction history.

Research state contains:

```text
question
clarifications
plan
tasks
evidence
notes
artifacts
report
evaluation
```

Do not overload chat history as a workflow database.

## 49. Enterprise Identity

Separate:

```text
human identity
tenant identity
AI-Q service identity
worker identity
connector identity
sandbox identity
```

## 50. OIDC

Validate:

```text
signature
issuer
audience
expiration
tenant claim
principal
roles/scopes
```

Do not trust tenant IDs from arbitrary request JSON in production.

## 51. RBAC

Examples:

```text
research_user
research_admin
source_admin
auditor
```

## 52. ABAC

Attributes may include:

```text
department
project
document classification
region
purpose
source
```

## 53. Multi-Tenancy

Tenant isolation must apply to:

```text
SQL
Redis
Kafka
vector indexes
OpenSearch
graph data
object storage
MCP
logs
traces
budgets
```

## 54. Prompt Injection

A retrieved document can contain:

```text
"ignore all previous instructions..."
```

That text remains data.

It cannot:

```text
grant permissions
enable a source
expose credentials
change system policy
disable citation verification
```

## 55. Indirect Injection

Web pages and search snippets are particularly hostile inputs.

Keep instructions and evidence in structurally separate channels and sanitize tool metadata.

## 56. Data Loss Prevention

Before enterprise content is sent to a model or external source:

```text
classify
redact/tokenize if required
check provider policy
check region
audit
```

## 57. Secrets

Use workload identity or short-lived brokered credentials.

Never place credentials in:

```text
prompts
research notes
memory
reports
logs
traces
artifacts
```

## 58. SSRF

Web and connector systems need:

```text
destination allowlists
DNS/IP checks
redirect revalidation
private-address blocking
metadata-endpoint blocking
```

## 59. Evidence Poisoning

Protect against malicious or low-quality sources by using source trust metadata, provenance, duplicate detection and cross-source corroboration.

## 60. Memory Poisoning

Do not automatically convert arbitrary research output into long-term enterprise memory.

Memory writes require provenance, classification, scope and retention policy.

## 61. Audit Trail

Record:

```text
requester
query
classification
selected sources
plan
tool invocations
models
evidence IDs
citation decisions
evaluation
report version
artifacts
timestamps
```

## 62. OpenTelemetry

A trace hierarchy can be:

```text
research.run
  classify
  clarify
  plan
  research.batch
    researcher
      source.search
      model.call
  evidence.merge
  write
  citations.verify
  evaluate
```

## 63. Metrics

Operational metrics:

```text
request rate
shallow/deep ratio
latency
queue lag
source errors
model errors
token usage
tool calls
cost
```

Quality metrics:

```text
citation coverage
citation correctness
source quality
freshness
completeness
contradiction handling
human acceptance
```

## 64. Logs

Use structured logs containing:

```text
trace_id
run_id
task_id
tenant
agent
source
model
latency
status
```

Never log secrets or unrestricted source content.

## 65. Evaluation Harness

Maintain:

```text
public benchmark suite
organization golden questions
adversarial questions
ACL tests
freshness tests
citation tests
```

Evaluate full workflow behavior rather than only model output.

## 66. Retrieval Evaluation

Measure:

```text
Recall@K
Precision@K
MRR
NDCG
reranker lift
ACL correctness
freshness
```

## 67. Research Evaluation

Measure:

```text
question coverage
evidence sufficiency
citation support
source diversity
contradiction handling
report structure
```

## 68. Regression Evaluation

Every change to:

```text
model
prompt
retriever
reranker
planner
source router
budget
```

should run the evaluation suite.

## 69. Freshness

Time-sensitive research needs an explicit research timestamp.

Evidence should preserve:

```text
publication date
retrieval date
source update date
```

## 70. Reproducibility

Persist:

```text
workflow version
model version
prompt version
source query
source metadata
evidence IDs
report hash
evaluation version
```

## 71. Caching

Cache only when authorization semantics are preserved.

Cache key should include relevant tenant/ACL context.

## 72. SQL Schema

Recommended production entities:

```text
research_runs
plan_versions
research_tasks
task_attempts
worker_leases
evidence
claims
claim_evidence
reports
report_versions
artifacts
source_registry
model_registry
idempotency_keys
outbox_events
audit_events
```

## 73. Database Indexes

Typical indexes:

```text
research_tasks(status, not_before)
research_tasks(run_id, task_key)
evidence(run_id, source_type)
reports(run_id, version)
outbox_events(published, created_at)
audit_events(run_id, created_at)
```

## 74. Transaction Boundaries

Never hold a SQL transaction open during:

```text
LLM call
web search
vector search
MCP call
sandbox execution
```

Persist intent, commit, perform network work, then persist result.

## 75. Alembic

Production uses explicit migrations.

Prefer expand/contract:

```text
add compatible schema
deploy compatible application
backfill
switch reads/writes
remove old schema later
```

## 76. Qdrant / Vector Store

The included Compose file provides Qdrant as a local vector infrastructure option.

Production considerations:

```text
tenant filters
payload ACLs
collection strategy
embedding version
replication
backup
capacity
```

## 77. OpenSearch

The included OpenSearch service represents lexical/enterprise-search infrastructure.

Production should enable authentication, TLS, access control, snapshots and resource sizing.

## 78. Knowledge Graph Store

A graph store is optional but useful for entity-centric and multi-hop research.

Examples of graph concepts:

```text
Company -> OWNS -> Product
Service -> DEPENDS_ON -> Service
Experiment -> USED_DATASET -> Dataset
Claim -> ABOUT -> Entity
```

## 79. Graph Safety

Do not treat model-inferred graph edges as verified facts unless backed by evidence.

## 80. SQL Research Gateway

Never provide unrestricted SQL credentials to an LLM.

Use:

```text
read-only role
allowed schemas
query parser/policy
timeout
row limit
cost limit
audit
```

## 81. cuDF Research Analysis

GPU dataframe acceleration is useful for large tabular evidence.

A governed analysis skill should:

```text
load authorized artifact
validate schema
run sandboxed analysis
record code/environment
write derived artifact
return evidence reference
```

## 82. Kubernetes Topology

```text
Ingress
  |
Research API
  |
Planner / Scheduler
  |
SQL + Outbox
  |
Kafka/Pulsar
  |
+-----------+----------+---------+---------+
|Retriever  |Researcher|Analysis |Writer   |
+-----------+----------+---------+---------+
  |
MCP / Search / RAG / SQL / Sandbox
```

## 83. Pod Classes

Separate:

```text
API pods
planner pods
researcher pods
writer pods
retriever pods
sandbox gateway
reconciliation
evaluation
```

This prevents one workload type from exhausting all resources.

## 84. Autoscaling

Useful signals:

```text
queue lag
oldest task age
research tasks waiting
source latency
model concurrency
sandbox demand
```

## 85. Multi-Region

Route based on:

```text
data residency
source locality
model availability
tenant policy
```

One region should own a task at a time.

## 86. Disaster Recovery

Recovery sequence:

```text
fence old workers
restore SQL
restore artifact metadata
replay unpublished outbox
restore source registry
reconcile running jobs
resume idempotent tasks
```

## 87. Backup

Back up:

```text
SQL
object storage
source configuration
workflow configuration
evaluation datasets
```

Vector indexes can sometimes be rebuilt, but rebuilding may be expensive.

## 88. Capacity Planning

Example variables:

```text
R = research requests/day
T = tasks/request
S = source calls/task
M = model calls/task
K = tokens/model call
```

Then estimate:

```text
source QPS ≈ R*T*S / active seconds
model calls/day ≈ R*T*M
tokens/day ≈ R*T*M*K
```

Deep research can be far more expensive than shallow lookup, so model the two separately.

## 89. Cost Governance

Track:

```text
model tokens
search API calls
retrieval compute
sandbox compute
GPU compute
artifact storage
```

Attribute costs to tenant and run.

## 90. Rate Limiting

Apply limits by:

```text
tenant
principal
source
model
MCP server
research depth
```

## 91. SLOs

Separate SLOs for:

```text
API availability
durable job acceptance
shallow response latency
deep job start latency
research completion
source availability
```

Do not define one latency SLO for both shallow and deep research.

## 92. Graceful Degradation

Possible degradation:

```text
graph unavailable -> lexical + vector
web provider unavailable -> enterprise-only report with limitation
writer model unavailable -> fallback approved writer
sandbox unavailable -> disable code analysis
```

Never silently bypass authorization.

## 93. CI/CD

Pipeline:

```text
lint
unit tests
property tests
contract tests
security scan
dependency scan
container scan
evaluation suite
integration tests
load tests
staging
progressive deployment
```

## 94. Unit Tests

Test:

```text
routing
DAG validation
budget logic
source authorization
citation validation
contradiction grouping
```

## 95. Property Tests

Important invariants:

```text
forbidden source never becomes evidence
citation references existing evidence
budget never grows beyond configured hard limit
one tenant cannot read another tenant's evidence
```

## 96. Contract Tests

Validate every model/source/MCP integration against expected schemas and failure semantics.

## 97. Load Tests

Test:

```text
many shallow requests
many simultaneous deep jobs
large source fan-out
slow models
slow search providers
large reports
```

## 98. Chaos Tests

Inject:

```text
worker death
duplicate event
Postgres failover
Redis loss
vector timeout
OpenSearch timeout
model timeout
MCP outage
```

Verify correctness, not merely service restart.

## 99. Security Tests

Test:

```text
cross-tenant retrieval
prompt injection
malicious document instructions
SSRF
credential exfiltration
citation substitution
source spoofing
sandbox escape
```

## 100. Application — Competitive Intelligence

```text
market question
 -> internal strategy/product evidence
 -> current external evidence
 -> competitor comparison
 -> contradiction analysis
 -> cited report
```

## 101. Application — Engineering Research

```text
architecture question
 -> internal docs/code/runbooks
 -> external technical sources
 -> evidence graph
 -> trade-off analysis
 -> design report
```

## 102. Application — Financial Research

Use strict:

```text
time period
currency
entity
filing date
source authority
```

for every material financial claim.

## 103. Application — Product Research

Combine:

```text
support tickets
feedback
analytics
roadmap documents
market evidence
```

without exposing private customer data beyond policy.

## 104. Application — Incident Investigation

Research:

```text
incident timeline
logs
runbooks
prior incidents
dependency status
external advisories
```

with explicit evidence lineage.

## 105. Application — Scientific Research

Track:

```text
paper
authors
publication date
dataset
method
result
limitations
replication evidence
```

## 106. Application — Executive Briefing

Deep research can produce a long report and then a concise executive synthesis referencing the same evidence graph.

## 107. Application — Due Diligence

Use separate workstreams for:

```text
company
market
technology
competition
risk
financial evidence
```

and explicitly surface evidence gaps.

## 108. Application — Enterprise Knowledge Assistant

Shallow research handles most quick questions; deep research activates for multi-document synthesis and analytical reports.

## 109. Report Follow-Up

A completed report can become governed context for:

```text
question answering
rewriting
executive summary
additional targeted research
```

Preserve report version and evidence lineage.

## 110. Run — Docker

```bash
cp .env.example .env
docker compose build
docker compose up -d
docker compose ps
curl http://localhost:8000/health
```

## 111. Run — Deep Research

```bash
curl -X POST http://localhost:8000/v1/research \
  -H 'x-api-key: change-me' \
  -H 'Content-Type: application/json' \
  --data-binary @examples/deep_research.json
```

## 112. Run — Shallow Research

```bash
curl -X POST http://localhost:8000/v1/research \
  -H 'x-api-key: change-me' \
  -H 'Content-Type: application/json' \
  --data-binary @examples/shallow_research.json
```

## 113. Run — Model Routes

```bash
curl http://localhost:8000/v1/models/routes \
  -H 'x-api-key: change-me'
```

## 114. Run — Host Development

```bash
docker compose up -d postgres redis qdrant opensearch
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Change service hostnames in `.env` to `localhost`, then:

```bash
uvicorn app.main:app --reload
```

## 115. Run — Tests

```bash
pytest -q
ruff check .
```

## 116. Run — Logs

```bash
docker compose logs -f api
docker compose logs -f postgres
docker compose logs -f qdrant
docker compose logs -f opensearch
```

## 117. Run — Database

```bash
docker compose exec postgres psql -U postgres -d aiq
```

```sql
\dt
SELECT * FROM research_runs;
SELECT * FROM research_tasks;
SELECT * FROM evidence;
SELECT * FROM claims;
SELECT * FROM outbox;
SELECT * FROM audit;
```

## 118. Run — Reset

```bash
docker compose down
```

To intentionally destroy local state:

```bash
docker compose down -v
```

## 119. Troubleshooting — 401

Ensure:

```text
x-api-key
```

matches `API_KEY` in `.env`.

## 120. Troubleshooting — Database

Inside Docker use hostname:

```text
postgres
```

From the host use:

```text
localhost
```

## 121. Troubleshooting — OpenSearch

Check:

```bash
curl http://localhost:9200
docker compose logs opensearch
```

For constrained development machines, increase Docker memory or temporarily run only the services needed by mock mode.

## 122. Troubleshooting — Qdrant

Check:

```bash
curl http://localhost:6333
docker compose logs qdrant
```

## 123. Troubleshooting — Research Budget

Inspect:

```text
MAX_RESEARCH_LOOPS
MAX_TASKS
MAX_SOURCES
MAX_MODEL_CALLS
MAX_TOOL_CALLS
MAX_BUDGET_USD
```

## 124. Troubleshooting — NVIDIA Credentials

Local mock mode does not require an NVIDIA API key.

Production model integration requires an approved NIM/Nemotron endpoint and credentials.

## 125. Code Walkthrough — `domain.py`

Defines:

```text
ResearchRequest
ResearchTask
ResearchPlan
Evidence
Claim
ResearchReport
```

These are the typed boundaries between orchestration stages.

## 126. Code Walkthrough — `planner.py`

Implements deterministic local shallow/deep planning.

In production, this is the boundary for a schema-constrained reasoning planner.

## 127. Code Walkthrough — `compiler.py`

Uses a directed graph to validate:

```text
unique tasks
dependency existence
acyclicity
```

Production extensions validate source/tool schemas, authorization, budgets and workflow versions.

## 128. Code Walkthrough — `retrieval.py`

Normalizes source results into `Evidence`.

Replace mock results with real enterprise/web/vector/graph adapters while preserving the same evidence contract.

## 129. Code Walkthrough — `source_policy.py`

Represents the pre-retrieval authorization boundary.

Production derives source permissions from trusted identity and policy, not user-provided JSON.

## 130. Code Walkthrough — `evidence_graph.py`

Maintains:

```text
evidence nodes
claim nodes
SUPPORTED_BY edges
```

Extend it with contradiction, derivation and entity relationships.

## 131. Code Walkthrough — `contradictions.py`

Provides a deterministic contradiction-analysis extension point.

Production can combine normalized structured comparison with model-assisted semantic contradiction classification.

## 132. Code Walkthrough — `citations.py`

Validates that claim citation IDs resolve to evidence actually collected by the workflow.

## 133. Code Walkthrough — `agents.py`

Contains:

```text
ResearchAgent
DataAnalysisAgent
CriticAgent
```

These are role boundaries; production can bind each role to separate model profiles and tool policies.

## 134. Code Walkthrough — `model_router.py`

Maps role and complexity to a provider/model profile.

Keep provider-specific credentials outside agents.

## 135. Code Walkthrough — `budget.py`

Bounds autonomy by research loops, tasks, sources, model/tool calls and monetary cost.

## 136. Code Walkthrough — `report.py`

Creates the report from evidence-linked claims.

A production writer model should receive only governed evidence and structured research state.

## 137. Code Walkthrough — `evaluator.py`

Measures citation coverage and contradictions and determines whether the workflow can pass or needs more research.

## 138. Code Walkthrough — `runtime.py`

Coordinates:

```text
plan
compile
retrieve
evidence graph
claim synthesis
contradiction detection
citation validation
critique
report
evaluation
```

It is intentionally easy to understand locally; the production design moves task execution to durable distributed workers.

## 139. Code Walkthrough — `models.py`

Provides durable SQL foundations for:

```text
research runs
tasks
evidence
claims
outbox
audit
```

## 140. Code Walkthrough — `api.py`

Exposes:

```text
POST /v1/research
GET /v1/models/routes
```

Production should add asynchronous job submission/status/events/artifacts/cancellation/report-follow-up endpoints.

## 141. Production API

Recommended:

```text
POST /v1/research/jobs
GET  /v1/research/jobs/{id}
GET  /v1/research/jobs/{id}/events
GET  /v1/research/jobs/{id}/report
GET  /v1/research/jobs/{id}/evidence
GET  /v1/research/jobs/{id}/artifacts
POST /v1/research/jobs/{id}/cancel
POST /v1/research/jobs/{id}/input
POST /v1/research/jobs/{id}/follow-up
```

## 142. Production Readiness Matrix

| Area | Local Reference | Production Target |
|---|---|---|
| Auth | API key | OIDC/workload identity |
| Planner | deterministic | schema-constrained LLM |
| Sources | mock | enterprise/web/MCP/RAG |
| Vector | service available | ACL-aware integration |
| Search | service available | secured integration |
| Runtime | in-process | SQL + outbox + workers |
| Queue | conceptual | Kafka/Pulsar |
| Evidence | in-memory response | durable evidence store |
| Artifacts | documented | S3-compatible storage |
| Models | routing profiles | NIM/Nemotron/frontier gateway |
| Audit | model exists | immutable event writes |
| Telemetry | documented | OpenTelemetry |
| Deployment | Compose | Helm/Kubernetes |
| Evaluation | basic | benchmark + golden corpus |

## 143. Production Upgrade Order

Recommended sequence:

```text
1 enterprise identity
2 retrieval ACLs
3 real source adapters
4 persistent state transitions
5 Alembic
6 outbox publisher
7 Kafka/Pulsar
8 distributed workers
9 leases/fencing/idempotency
10 durable evidence/artifacts
11 real model gateway
12 citation verification hardening
13 OpenTelemetry
14 asynchronous jobs API
15 Kubernetes/Helm
16 load/chaos/security evaluation
17 DR exercises
```

## 144. Principal-Level Design Questions

Be ready to explain:

```text
Why shallow + deep?
Why planner/researcher/writer separation?
How do you prevent source-router privilege escalation?
How do citations remain trustworthy?
How do you handle contradictory sources?
How do you bound deep-research cost?
How do you resume a 10-minute job after worker failure?
How do you isolate tenants?
How do you prevent prompt injection from enterprise docs?
How do you evaluate research quality?
How do you scale to thousands of concurrent jobs?
```

## 145. Final Architecture Principle

```text
LLM             -> reasoning
Intent Router   -> depth
Planner         -> structured research
Policy          -> authority
Retriever       -> authorized evidence
Evidence Graph  -> provenance
Researcher      -> evidence interpretation
Critic          -> gaps and conflicts
Writer          -> synthesis
Citation Engine -> claim/evidence binding
Evaluator       -> quality
Budget Manager  -> bounded autonomy
Durable Runtime -> execution truth
Audit           -> reconstruction
```

A trustworthy enterprise research system is not defined by how many agents it has. It is defined by whether every important claim can be traced to authorized evidence, every consequential capability is governed, and every long-running research job can be bounded, evaluated, resumed and audited.
