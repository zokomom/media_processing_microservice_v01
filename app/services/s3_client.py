import boto3
from app.config import S3_BUCKET_NAME

s3 = boto3.client("s3")

BUCKET_NAME = S3_BUCKET_NAME


def upload_to_s3(local_path, s3_key):
    s3.upload_file(
        local_path,
        BUCKET_NAME,
        s3_key
    )


def download_from_s3(s3_key, local_path):
    s3.download_file(
        BUCKET_NAME,
        s3_key,
        local_path
    )

def generate_presigned_url(s3_key):
    return s3.generate_presigned_url(
        ClientMethod="get_object",
        Params={
            "Bucket": S3_BUCKET_NAME,
            "Key": s3_key
        },
        ExpiresIn=3600
    )