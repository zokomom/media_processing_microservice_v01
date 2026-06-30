from app.celery_app import celery_app
from app.services.image_service import (
    resize_image,
    compress_video,
    generate_thumbnail
)
from .services.job_services import update_job_status


@celery_app.task
def process_image(filename, job_id):
    update_job_status(job_id, "processing")
    try:
        print(f"Processing image: {filename}")
        resize_image(filename)
        update_job_status(job_id, "completed")
        print(f"Completed image: {filename}")
    except Exception as e:
        update_job_status(job_id, "failed")
        print(f"Error while processing {filename}: {e}")
        raise


@celery_app.task
def process_video(filename, job_id):
    update_job_status(job_id, "processing")
    try:
        print(f"Processing video: {filename}")
        compress_video(filename)
        generate_thumbnail(filename)
        update_job_status(job_id, "completed")
        print(f"Completed video: {filename}")
    except Exception as e:
        update_job_status(job_id, "failed")
        print(f"Error while processing {filename}: {e}")
        raise
