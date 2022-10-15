
# Tool: Janssen EDetail Generator
# Description: This tool helps in generating all required files by reading requirement from excel file .
# Author: Mohammed Nabeel P
# Version: 1.4.5(Development Tool)

import openpyxl
import shutil
from file_handlers import createHtml, createConfig, renameSharedFiles, generateCssJs as gCJ, imageResize as IR, generateSharedHtml
import os


class Error(Exception):
    pass


class projectNameError(Error):
    pass


class imageFileError(Error):
    pass


class popupError(Error):
    pass


try:
    book = openpyxl.load_workbook("./data.xlsx")
    data = book.active
    project_name = data['A2'].value
    if project_name == None or project_name == '':
        raise projectNameError
    source_folder = "./boiler_plate/slide"
    image_folder = "./images"
    shared_src = "./boiler_plate/shared"
    shared_dest = f"./output/{project_name}/shared"
    config_dest = f"./output/{project_name}/shared/{project_name}_SharedResource/common"
    slide_names = []
    project_id = project_name.split('_')[0]

    for i in range(data.max_row-1):
        folder_name = f'{project_name}_S{str(i+1)}_{(data[f"B{i+2}"].value).replace(" ","_")}'
        slide_names.append(folder_name)
        popups = data[f'D{i+2}'].value
        if (popups != None):
            popups = popups.split(',')
        else:
            popups = ''
        destination_folder = f"./output/{project_name}/{folder_name}"

        if not os.path.exists(destination_folder):
            shutil.copytree(source_folder, destination_folder)

        createHtml(project_id, folder_name, project_name,
                   destination_folder, i+1, len(popups))
        gCJ(destination_folder, popups, i+1)
        # ========= Images ===========
        try:
            img_name = f'{image_folder}/{data[f"C{i+2}"].value}.jpg'
            IR(img_name, (2048, 1536), f'{destination_folder}/img/main.jpg')
            IR(img_name, (1024, 768),
                f'{destination_folder}/{folder_name}-full.jpg')
            IR(img_name, (200, 150),
                f'{destination_folder}/{folder_name}-thumb.jpg')
        except:
            raise imageFileError
        # ========= popups ===========
        try:
            for popup in popups:
                IR(f'{image_folder}/{popup}.jpg', (2048, 1536),
                   f'{destination_folder}/img/{popup}.jpg')
        except:
            raise popupError

    if not os.path.exists(shared_dest):
        shutil.copytree(shared_src, shared_dest)
    sharedHTML = renameSharedFiles(shared_dest, project_name,
                                   f'{image_folder}/{data["C2"].value}.jpg')
    generateSharedHtml(project_id, sharedHTML)
    createConfig(project_name, slide_names, config_dest)

except imageFileError:
    print('ERROR : images - Check slide names in Excel or "images" folder is missing')
except projectNameError:
    print('ERROR : Project name should not be empty in Excel')
except popupError:
    print('ERROR : Popup images are missing or wrong names in Excel ')
except FileNotFoundError:
    print(
        "ERROR : Make sure ['images','boiler_plate','data.xlsx'] are present in same folder")
print('Process Finished')
