
run:
	gunicorn test:app -b 0.0.0.0:8000 --worker-class=uvicorn.workers.UvicornWorker --workers=5
