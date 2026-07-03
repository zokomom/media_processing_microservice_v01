from celery import Celery
from .config import RABBITMQ_URL

celery_app = Celery(
    "media_tasks",
    broker=RABBITMQ_URL,
    include=["app.tasks"]
)
