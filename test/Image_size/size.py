from PIL import Image

img = './main.jpg'
size = (1024, 768)
dest = 'good'


def imageResize(image, size, dest):
    img = Image.open(image)
    new_image = img.resize(size)
    new_image.save(dest)
    return 'Image resized'


imageResize(img, size, f'{dest}-full.jpg')
imageResize(img, (200, 150), f'{dest}-thumb.jpg')
