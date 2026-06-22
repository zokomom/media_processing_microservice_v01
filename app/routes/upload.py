from fastapi import APIRouter,UploadFile,File,status,HTTPException
from ..services.image_service import compress_video, resize_image
from ..services.s3_client import upload_to_s3
import uuid

router = APIRouter()

@router.post("/upload",status_code=201)
async def upload_file(file: UploadFile = File(...)):

    extension = file.filename.split(".")[-1]

    filename = f"{uuid.uuid4()}.{extension}"

    local_path = f"app/uploads/{filename}"

    content = await file.read()
    
    with open(local_path,"wb") as f:
        f.write(content)
    
    upload_to_s3(
        local_path,
        f"uploads/{filename}"
    )
    
    if file.content_type.startswith("image/"):
        resize_image(filename)
    else:
        compress_video(filename)

    return {"message": "File uploaded and processed successfully"}
