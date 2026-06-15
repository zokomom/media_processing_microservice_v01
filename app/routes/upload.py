from fastapi import APIRouter,UploadFile,File,status,HTTPException
from ..services.image_service import compress_video, resize_image

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    content = await file.read()

    with open(f"app/uploads/{file.filename}","wb") as f:
        f.write(content)

    if file.content_type.startswith("image/"):
        resize_image(file.filename)
    else:
        compress_video(file.filename)
    
    return {"message": "File uploaded and processed successfully"}
