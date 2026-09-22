test:
	PYTHONPATH=. pytest -q
api:
	uvicorn apps.api.src.main:app --reload --port 8000
