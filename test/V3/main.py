
# Tool: Janssen EDetail Generator
# Description: This tool helps in generating all required files by reading requirement from excel file .
# Author: Mohammed Nabeel P
# Version: 3.0.0(Development Tool)
import time
from pdf2image import convert_from_path

start_time = time.time()
import openpyxl
import shutil
from file_handlers import createHtml, createConfig, renameSharedFiles, generateCssJs as gCJ, imageResize as IR, generateSharedHtml
import os
import ctypes


class Error(Exception):
    pass


class projectNameError(Error):
    pass


class imageFileError(Error):
    pass


class popupError(Error):
    pass


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)



book = openpyxl.load_workbook("./data_pdf.xlsx")
data = book.active
pdf = './pdf/test.pdf'
pdf_images = convert_from_path(
    pdf, poppler_path=r'poppler-22.04.0\Library\bin', size=(2048, 1536))

project_name = data['A2'].value
project_id = project_name.split('_')[0]
if project_name == None or project_name == '':
    raise projectNameError
source_folder = "./boiler_plate/slide"
image_folder = "./images"
for i in range(len(pdf_images)):
    pdf_images[i].save(image_folder+'/Slide_'+ str(i+1) + '.jpg', 'JPEG')
shared_src = "./boiler_plate/shared"
shared_dest = f"./output/{project_name}/shared"
config_dest = f"./output/{project_name}/shared/{project_id}_SharedResource/common"
slide_names = []
carousal_slides =[]
max_row = 0
for row in data:
    if not all([cell.value is None for cell in row]):
        max_row += 1
for i in range(max_row-1):
    folder_name = f'{project_name}_S{str(i+1)}_{(data[f"B{i+2}"].value).replace(" ","_")}'

    slide_names.append(folder_name)
    popups = data[f'D{i+2}'].value
    buttons = data[f'E{i+2}'].value
    slides = str(data[f"C{i+2}"].value).split(',')
    slides = [f'Slide_{x}.jpg' for x in slides] 
   
    if len(slides)>1:
        carousal_slides.append(f"s{i+1}")
    if (popups != None):
        popups = str(popups).split(',')
        popups = [f'Slide_{x}.jpg' for x in popups] 
    else:
        popups = ''
    if (buttons != None):
        buttons = buttons.split(',')
    else:
        buttons = ''
    
    destination_folder = f"./output/{project_name}/{folder_name}"

    if not os.path.exists(destination_folder):
        shutil.copytree(source_folder, destination_folder)

    createHtml(project_id, folder_name,
                destination_folder, i+1,slides, len(popups),buttons)
    gCJ(destination_folder,slides, popups, i+1)
    # ========= Images ===========
    try:
        for slide in  slides:    
            img_name = f'{image_folder}/{slide}'
            IR(img_name, (2048, 1536), f'{destination_folder}/img/{slide}')
        img_name = f'{image_folder}/{slides[0]}'
        IR(img_name, (1024, 768),
            f'{destination_folder}/{folder_name}-full.jpg')
        IR(img_name, (200, 150),
            f'{destination_folder}/{folder_name}-thumb.jpg')
    except:
        raise imageFileError
    # ========= popups ===========
    try:
        for popup in popups:
            IR(f'{image_folder}/{popup}', (2048, 1536),
                f'{destination_folder}/img/{popup}')
    except:
        raise popupError

if not os.path.exists(shared_dest):
    shutil.copytree(shared_src, shared_dest)
shared_image =f'Slide_{str(data["C2"].value)[0]}.jpg'
sharedHTML = renameSharedFiles(shared_dest, project_id,
                                f'{image_folder}/{shared_image}')
generateSharedHtml(project_id, sharedHTML)
createConfig(project_name,carousal_slides, slide_names, config_dest)


print("--- %s seconds ---" % (time.time() - start_time))
print('Process Finished')
Mbox(f'Hurray Process Finished successfully !',
     'Check output folder for output.....', 0x40)
