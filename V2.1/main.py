
# Tool: Janssen EDetail Generator
# Description: This tool helps in generating all required files by reading requirement from excel file .
# Author: Mohammed Nabeel P
# Version: 1.4.5(Development Tool)

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


try:
    book = openpyxl.load_workbook("./data.xlsx")
    data = book.active
    project_name = data['A2'].value
    project_id = project_name.split('_')[0]
    if project_name == None or project_name == '':
        raise projectNameError
    source_folder = "./boiler_plate/slide"
    image_folder = "./images"
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
        slides = (data[f"C{i+2}"].value).split(',')
        if len(slides)>1:
            carousal_slides.append(f"s{i+1}")
        if (popups != None):
            popups = popups.split(',')
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
    sharedHTML = renameSharedFiles(shared_dest, project_id,
                                    f'{image_folder}/{(data["C2"].value).split(",")[0]}')
    generateSharedHtml(project_id, sharedHTML)
    createConfig(project_name,carousal_slides, slide_names, config_dest)

except imageFileError:
    print('ERROR : images - Check slide names in Excel or "images" folder is missing')
    Mbox('ERROR',
         "images - Check slide names in Excel or 'images' folder is missing", 0x30)
except projectNameError:
    print('ERROR : Project name should not be empty in Excel')
    Mbox('ERROR',
         "Project name should not be empty in Excel", 0x30)
except popupError:
    print('ERROR : Popup images are missing or wrong names in Excel ')
    Mbox('ERROR',
         "Popup images are missing or wrong names in Excel", 0x30)
except FileNotFoundError:
    print(
        "ERROR : Make sure ['images','boiler_plate','data.xlsx'] are present in same folder or some files are missing in boiler_plate")
    Mbox('ERROR',
         "Make sure ['images','boiler_plate','data.xlsx'] are present in same folder or some files are missing in boiler_plate folder.check readme file for folder stucture", 0x20)

except:
    Mbox(f'ERROR !',
         'Something went wrong.....', 0x20)


print('Process Finished')
Mbox(f'Hurray Process Finished successfully !',
     'Check output folder for output.....', 0x40)
