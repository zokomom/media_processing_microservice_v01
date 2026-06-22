from PIL import Image
import ffmpeg
from ..services.s3_client import upload_to_s3

def resize_image(filename):

    img = Image.open(f"app/uploads/{filename}")

    img = img.resize((500,500))

    img.save(f"app/processed/{filename}")

    upload_to_s3(
        f"app/processed/{filename}",
        f"processed/{filename}"
    )

def compress_video(filename):
    ffmpeg.input(f"app/uploads/{filename}").output(
        f"app/processed/{filename}",
        vcodec="libx264"
    ).run()

    upload_to_s3(
        f"app/processed/{filename}",
        f"processed/{filename}"
    )
