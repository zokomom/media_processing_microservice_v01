from PIL import Image
import ffmpeg
from ..services.s3_client import upload_to_s3, download_from_s3


def resize_image(filename):

    local_input = f"/tmp/{filename}"

    download_from_s3(
        f"uploads/{filename}",
        local_input
    )

    img = Image.open(local_input)

    img = img.resize((500, 500))

    img.save(f"app/processed/{filename}")

    local_output = f"/tmp/processed_{filename}"

    img.save(local_output)

    upload_to_s3(
        local_output,
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
