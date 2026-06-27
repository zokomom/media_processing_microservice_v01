from app.celery_app import celery_app
from app.services.image_service import (
    resize_image,
    compress_video,
    generate_thumbnail
)


@celery_app.task
def process_image(filename):
    print(f"Processing image: {filename}")
    resize_image(filename)
    print(f"Completed image: {filename}")


@celery_app.task
def process_video(filename):
    print(f"Processing video: {filename}")
    compress_video(filename)
    generate_thumbnail(filename)
    print(f"Completed video: {filename}")
