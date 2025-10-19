from PIL import Image
import io

def image_to_blob(image_path):
    with Image.open(image_path) as img:
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format=img.format or 'PNG')
        return img_byte_arr.getvalue()

blob_data = image_to_blob('img.png')

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(str(blob_data))