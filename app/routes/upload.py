from fastapi import APIRouter, UploadFile, File, status, HTTPException
from ..services.image_service import compress_video, resize_image
from ..services.s3_client import upload_to_s3
import uuid
from app.tasks import process_image, process_video
from ..services.job_services import create_job

router = APIRouter()


@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_file(file: UploadFile = File(...)):

    extension = file.filename.split(".")[-1]

    filename = f"{uuid.uuid4()}.{extension}"

    job_id = create_job()

    local_path = f"app/uploads/{filename}"

    content = await file.read()

    with open(local_path, "wb") as f:
        f.write(content)

    upload_to_s3(
        local_path,
        f"uploads/{filename}"
    )

    if file.content_type.startswith("image/"):
        process_image.delay(filename, job_id)
    else:
        process_video.delay(filename, job_id)

    return {
        "message": "File uploaded successfully",
        "job_id": job_id,
        "status": "queued"
    }
