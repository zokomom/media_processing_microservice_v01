import boto3

s3 = boto3.client("s3")

BUCKET_NAME ="atharv-media-storage"

def upload_to_s3(local_path, s3_key):
    s3.upload_file(
        local_path,
        BUCKET_NAME,
        s3_key
    )