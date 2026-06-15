from PIL import Image

def resize_image(filename):

    img = Image.open(f"uploads/{filename}")

    img = img.resize((500,500))

    img.save(f"processed/{filename}")