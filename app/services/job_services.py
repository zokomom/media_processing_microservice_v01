import redis
import json
import uuid

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=1,
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


def update_job_status(job_id: str, status: str):
    job = redis_client.get(job_id)

    if not job:
        return

    job = json.loads(job)

    job["status"] = status

    redis_client.set(
        job_id,
        json.dumps(job)
    )


def get_job(job_id: str):
    job = redis_client.get(job_id)
    if not job:
        return None
    return json.loads(job)
