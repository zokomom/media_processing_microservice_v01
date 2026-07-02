from PIL import Image, ImageDraw, ImageFont


def crop_center(img: Image.Image) -> Image.Image:

    width, height = img.size
    crop_size = min(width, height)
    left = (width - crop_size) // 2
    top = (height - crop_size) // 2
    right = left + crop_size
    bottom = top + crop_size

    return img.crop((left, top, right, bottom))


def resize_to_square(img: Image.Image, size: int = 500) -> Image.Image:
    return img.resize((size, size))


def add_watermark(img):
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    draw.text((420, 480), "© Atharv", fill="white", font=font)

    return img
