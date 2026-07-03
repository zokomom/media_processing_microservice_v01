from PIL import Image,ImageOps
import ffmpeg
from ..services.s3_client import upload_to_s3, download_from_s3
from ..utils.img_utils import crop_center, resize_to_square, add_watermark
import os


def resize_image(filename):

    local_input = f"/tmp/{filename}"
    local_output = f"/tmp/processed_{filename}"

    download_from_s3(f"uploads/{filename}", local_input)
    with Image.open(local_input) as img:
        img.save("/tmp/debug.jpg")
        img = ImageOps.exif_transpose(img)

        img = crop_center(img)
        img = resize_to_square(img)
        img = add_watermark(img)
        img.save(local_output, optimize=True, quality=75)

    try:
        upload_to_s3(
            local_output,
            f"processed/{filename}"
        )
    finally:
        if os.path.exists(local_input):
            os.remove(local_input)

        if os.path.exists(local_output):
            os.remove(local_output)


def compress_video(filename):
    local_input = f"/tmp/{filename}"

    download_from_s3(
        f"uploads/{filename}",
        local_input
    )

    local_output = f"/tmp/processed_{filename}"

    ffmpeg.input(local_input).output(local_output, vcodec="libx264").run(
        overwrite_output=True, quiet=True)

    try:
        upload_to_s3(
            local_output,
            f"processed/{filename}"
        )
    finally:
        if os.path.exists(local_input):
            os.remove(local_input)

        if os.path.exists(local_output):
            os.remove(local_output)


def generate_thumbnail(filename):

    local_video = f"/tmp/{filename}"

    thumbnail_name = filename.rsplit(".", 1)[0] + ".jpg"

    local_thumbnail = f"/tmp/{thumbnail_name}"

    download_from_s3(
        f"uploads/{filename}",
        local_video
    )

    ffmpeg.input(local_video, ss=1).output(
        local_thumbnail, vframes=1).overwrite_output().run(overwrite_output=True, quiet=True)

    try:
        upload_to_s3(
            local_thumbnail,
            f"thumbnails/{thumbnail_name}"
        )

    finally:
        if os.path.exists(local_video):
            os.remove(local_video)

        if os.path.exists(local_thumbnail):
            os.remove(local_thumbnail)
