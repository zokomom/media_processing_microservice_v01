from celery import Celery
from .config import REDIS_URL

celery_app = Celery(
    "media_tasks",
    broker=REDIS_URL,
    include=["app.tasks"]
)
