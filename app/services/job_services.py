import redis
import json
import uuid
from app.config import REDIS_URL

redis_client = redis.from_url(
    REDIS_URL,
    decode_responses=True
)


def create_job():

    job_id = str(uuid.uuid4())

    redis_client.set(
        job_id,
        json.dumps({
            "status": "queued"
        })
    )
    return job_id


def update_job_status(job_id: str, status: str,**kwargs):
    job = redis_client.get(job_id)

    if not job:
        return

    job = json.loads(job)

    job["status"] = status

    job.update(kwargs)

    redis_client.set(
        job_id,
        json.dumps(job)
    )


def get_job(job_id: str):
    job = redis_client.get(job_id)
    if not job:
        return None
    return json.loads(job)
