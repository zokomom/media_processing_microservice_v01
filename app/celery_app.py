from celery import Celery

celery_app = Celery(
    "media_tasks",
    broker="redis://localhost:6379/0",
    include=["app.tasks"]
)
