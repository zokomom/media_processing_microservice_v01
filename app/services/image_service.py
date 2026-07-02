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

    img.save(local_output, optimize=True, quality=75)

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


def generate_thumbnail(filename):

    local_video = f"/tmp/{filename}"

    thumbnail_name = filename.rsplit(".", 1)[0] + ".jpg"

    local_thumbnail = f"/tmp/{thumbnail_name}"

    download_from_s3(
        f"uploads/{filename}",
        local_video
    )

    ffmpeg.input(local_video, ss=1).output(
        local_thumbnail, vframes=1).overwrite_output().run()

    upload_to_s3(
        local_thumbnail,
        f"thumbnails/{thumbnail_name}"
    )
