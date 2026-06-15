from PIL import Image

def resize_image(filename):
    
    img = Image.open(f"app/uploads/{filename}")

    img = img.resize((500,500))

    img.save(f"app/processed/{filename}")