import PIL
from PIL import Image
import os 

path= 'source/'
export_path = 'dest/'

images = os.listdir(path)

def resize():
    for image in images:
        image_name = image.split('.', 1)[0]
        fixed_height = 1024
        image = Image.open(path+image)
        height_percent = (fixed_height / float(image.size[1]))
        width_size = int( float(image.size[0]) * float(height_percent) )
        image = image.resize((width_size, fixed_height), PIL.Image.NEAREST)
        image.save(export_path+image_name+ '.webp', 'webp', optimize=True, quality=90)

resize() 