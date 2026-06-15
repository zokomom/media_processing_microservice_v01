from fastapi import APIRouter,UploadFile, File
from ..services.image_service import resize_image

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    with open(f"uploads/{file.filename}","wb") as f:
        f.write(content)
    resize_image(file.filename)
    return {"message": "File uploaded and processed successfully"}
