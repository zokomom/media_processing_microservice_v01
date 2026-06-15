from PIL import Image
import ffmpeg

def resize_image(filename):

    img = Image.open(f"app/uploads/{filename}")

    img = img.resize((500,500))

    img.save(f"app/processed/{filename}")

def compress_video(filename):
    ffmpeg.input(f"app/uploads/{filename}").output(
        f"app/processed/{filename}",
        vcodec="libx264"
    ).run()
