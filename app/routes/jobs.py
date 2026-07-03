from fastapi import APIRouter, HTTPException

from app.services.job_services import get_job

from app.services.s3_client import generate_presigned_url

router = APIRouter()


@router.get("/jobs/{job_id}")
def get_job_status(job_id: str):
    job = get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    if "processed_key" in job:
        job["download_url"] = generate_presigned_url(
            job["processed_key"]
        )

    if "thumbnail_key" in job:
        job["thumbnail_url"] = generate_presigned_url(
            job["thumbnail_key"]
        )
    
    job.pop("processed_key", None)
    job.pop("thumbnail_key", None)

    return job
