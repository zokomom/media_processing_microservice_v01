from dotenv import load_dotenv
import os

load_dotenv()

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

REDIS_URL = os.getenv("REDIS_URL")

RABBITMQ_URL = os.getenv("RABBITMQ_URL")
