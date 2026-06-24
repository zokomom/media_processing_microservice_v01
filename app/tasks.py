from app.celery_app import celery_app
from app.services.image_service import (
    resize_image,
    compress_video
)


@celery_app.task
def process_image(filename):
    print(f"Processing image: {filename}")
    resize_image(filename)
    print(f"Completed image: {filename}")


@celery_app.task
def process_video(filename):
    compress_video(filename)
