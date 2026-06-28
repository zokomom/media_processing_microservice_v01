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
