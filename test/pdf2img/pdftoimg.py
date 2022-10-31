from pdf2image import convert_from_path
images = convert_from_path(
    './pdf.pdf', poppler_path=r'poppler-22.04.0\Library\bin', size=(2048, 1536))

for i in range(len(images)):
    images[i].save('out/page' + str(i) + '.jpg', 'JPEG')
