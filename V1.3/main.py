import openpyxl
import shutil
from file_handlers import createHtml, createConfig, renameSharedFiles, generateCssJs as gCJ, imageResize as IR

book = openpyxl.load_workbook("./data.xlsx")
data = book.active
project_name = data['A2'].value
source_folder = "./boiler_plate/slide"
image_folder = "./images"
shared_src = "./boiler_plate/shared"
shared_dest = f"./{project_name}/shared"
config_dest = f"./{project_name}/shared/{project_name}_SharedResource/common"
slide_names = []
project_id = project_name.split('_')[0]

for i in range(data.max_row-1):
    folder_name = f'{project_name}_S{str(i+1)}_{(data[f"B{i+2}"].value).replace(" ","_")}'
    slide_names.append(folder_name)
    destination_folder = f"./{project_name}/{folder_name}"
    shutil.copytree(source_folder, destination_folder)
    popup = data[f"D{i+2}"].value
    createHtml(project_id, folder_name, project_name,
               destination_folder, i+1, popup)
    gCJ(destination_folder)
# ========= Images ===========
    # img_name = f'{data[f"C{i+2}"].value}'
    img_name = f'{image_folder}/{data[f"C{i+2}"].value}.jpg'
    IR(img_name, (2048, 1536), f'{destination_folder}/img/main.jpg')
    IR(img_name, (1024, 768), f'{destination_folder}/{folder_name}-full.jpg')
    IR(img_name, (200, 150), f'{destination_folder}/{folder_name}-thumb.jpg')
    # shutil.copy(
    #     f'{image_folder}/main/{data[f"C{i+2}"].value}.jpg', f'{destination_folder}/img/main.jpg')
    # shutil.copy(
    #     f'{image_folder}/full/{img_name}.jpg', f'{destination_folder}/{folder_name}-full.jpg')
    # shutil.copy(
    #     f'{image_folder}/thumb/{img_name}.jpg', f'{destination_folder}/{folder_name}-thumb.jpg')

shutil.copytree(shared_src, shared_dest)
renameSharedFiles(shared_dest, project_name)
createConfig(project_name, slide_names, config_dest)
print('Folders created')
