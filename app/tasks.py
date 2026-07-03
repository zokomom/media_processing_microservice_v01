from app.celery_app import celery_app
from app.services.image_service import (
    resize_image,
    compress_video,
    generate_thumbnail
)
from .services.job_services import update_job_status


@celery_app.task(bind=True, max_retries=3)
def process_image(self, filename, job_id):
    update_job_status(job_id, "processing")
    try:
        print(f"Processing image: {filename}")
        resize_image(filename)
        update_job_status(job_id, "completed",processed_key=f"processed/{filename}")
        print(f"Completed image: {filename}")
    except Exception as e:
        if self.request.retries >= self.max_retries:
            print("Maximum retries exceeded.")
            update_job_status(job_id, "failed")
            raise

        print(f"Retry #{self.request.retries + 1}")
        raise self.retry(exc=e, countdown=5)


@celery_app.task(bind=True, max_retries=3)
def process_video(self, filename, job_id):
    update_job_status(job_id, "processing")
    try:
        print(f"Processing video: {filename}")
        compress_video(filename)
        generate_thumbnail(filename)
        thumbnail_name = filename.rsplit(".", 1)[0] + ".jpg"
        update_job_status(job_id, "completed",processed_key=f"processed/{filename}",thumbnail_key=f"thumbnails/{thumbnail_name}")
        print(f"Completed video: {filename}")
    except Exception as e:
        if self.request.retries >= self.max_retries:
            print("Maximum retries exceeded.")
            update_job_status(job_id, "failed")
            raise

        print(f"Retry #{self.request.retries + 1}")
        raise self.retry(exc=e, countdown=5)
