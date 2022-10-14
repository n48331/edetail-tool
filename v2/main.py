import openpyxl
import shutil
from file_handlers import createHtml, createConfig, renameSharedFiles, generateCssJs as gCJ

book = openpyxl.load_workbook("./data.xlsx")
data = book.active
project_name = data['A2'].value
source_folder = "./boiler_plate/slide"
image_folder = "./images"
shared_src = "./boiler_plate/shared"
shared_dest = f"./{project_name}/shared"
config_dest = f"./{project_name}/shared/{project_name}_SharedResource/common"
slide_names = []


for i in range(data.max_row-1):
    folder_name = f'{project_name}_S{str(i+1)}_{(data[f"B{i+2}"].value).replace(" ","_")}'
    slide_names.append(folder_name)
    destination_folder = f"./{project_name}/{folder_name}"
    shutil.copytree(source_folder, destination_folder)
    createHtml(folder_name, project_name, destination_folder, i+1)
    gCJ(destination_folder)
# ========= Images ===========
    shutil.copy(
        f'{image_folder}/{data[f"C{i+2}"].value}.jpg', f'{destination_folder}/img/main.jpg')

shutil.copytree(shared_src, shared_dest)
renameSharedFiles(shared_dest, project_name)
createConfig(project_name, slide_names, config_dest)
print('Folders created')
