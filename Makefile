up:
	docker compose up --build -d
down:
	docker compose down
test:
	pytest -q
lint:
	ruff check .
run:
	uvicorn app.main:app --reload
