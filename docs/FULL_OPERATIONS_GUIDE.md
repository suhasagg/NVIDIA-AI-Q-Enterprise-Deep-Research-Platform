# Full Operations Guide

## Local
```bash
cp .env.example .env
docker compose up --build -d
curl http://localhost:8000/health
curl -X POST http://localhost:8000/v1/research -H 'x-api-key: change-me' -H 'Content-Type: application/json' --data-binary @examples/deep_research.json
pytest -q
```

## Production
Use OIDC/workload identity, ACL-aware retrieval, Alembic, SQL state transitions, transactional outbox, Kafka/Pulsar, distributed workers, leases/fencing/idempotency, durable evidence/artifacts, NIM/Nemotron model gateway, OpenTelemetry, Kubernetes and organization-specific evaluation.

## Incident Rule
Preserve durable research state, stop unsafe dispatch, fence stale workers, preserve evidence provenance, reconcile unfinished tasks and resume only idempotent work.
