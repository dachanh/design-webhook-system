export DATABASE_URL=postgresql://root:secret@127.0.0.1:5434/webhook?sslmode=disable && celery -A task.upload_file.celery worker --loglevel=info
celery --broker=redis://127.0.0.1:6379/0 flower  -A tasks

