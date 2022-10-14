import openpyxl
import shutil
from file_handlers import createHtml
from file_handlers import renameSharedFiles
from file_handlers import generateCssJs as gCJ

book = openpyxl.load_workbook("./data.xlsx")
data = book.active
project_name = data['A2'].value
source_folder = "./boiler_plate/slide"
shared_src = "./boiler_plate/shared"
shared_dest = f"./{project_name}/shared"
slide_names = []


for i in range(data.max_row-1):
    folder_name = f'{project_name}_S{str(i+1)}_{(data[f"B{i+2}"].value).replace(" ","_")}'
    slide_names.append(folder_name)
#     destination_folder = f"./{project_name}/{folder_name}"
#     shutil.copytree(source_folder, destination_folder)
#     createHtml(folder_name, destination_folder)
#     gCJ(destination_folder)

# shutil.copytree(shared_src, shared_dest)
# renameSharedFiles(shared_dest, project_name)

print('Folders created')
print(slide_names)
