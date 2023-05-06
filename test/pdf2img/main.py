import time
from pdf2image import convert_from_path
start_time = time.time()


images = convert_from_path(
    './pdf.pdf', poppler_path=r'poppler-22.04.0\Library\bin', size=(2048, 1536))
images = convert_from_path(
    './pdf.pdf', poppler_path=r'poppler-22.04.0\Library\bin', size=(1024, 768))
images = convert_from_path(
    './pdf.pdf', poppler_path=r'poppler-22.04.0\Library\bin', size=(200, 150))
print(images)
# def imageResize(image=images[1], size=(1024, 768), dest='1.jpg'):
#     image.convert('RGB').resize(size).save(f'{dest}')
#     return 'Image resized'
    # for i in range(len(images)):
    # images[0].save('out/page' + str(0) + '.jpg', 'JPEG')
    # print('one don')
    # images[1].save('out/page' + str(1) + '.jpg', 'JPEG')
    # images[2].save('out/page' + str(2) + '.jpg', 'JPEG')
images[3].save('out/page' + str(3) + '.jpg', 'JPEG')
    # images[4].save('out/page' + str(4) + '.jpg', 'JPEG')
    # images[5].save('out/page' + str(5) + '.jpg', 'JPEG')
    # images[6].save('out/page' + str(6) + '.jpg', 'JPEG')
# imageResize()
print("--- %s seconds ---" % (time.time() - start_time))
