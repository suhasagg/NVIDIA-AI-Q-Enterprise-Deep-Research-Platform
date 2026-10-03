# Runbook

```bash
cp .env.example .env
docker compose up --build -d
curl http://localhost:8000/health
curl -X POST http://localhost:8000/v1/research -H 'x-api-key: change-me' -H 'Content-Type: application/json' --data-binary @examples/deep_research.json
docker compose logs -f api
pytest -q
```
