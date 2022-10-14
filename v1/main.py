import openpyxl
import shutil
from file_generators import createHtml
from file_generators import generateCssJs as gCJ

book = openpyxl.load_workbook("./data.xlsx")
data = book.active
project_name = data['A2'].value
source_folder = "./boiler_plate"

for i in range(data.max_row-1):
    folder_name = f'{project_name}_S{str(i+1)}_{(data[f"B{i+2}"].value).replace(" ","_")}'
    destination_folder = f"./{project_name}/{folder_name}"
    shutil.copytree(source_folder, destination_folder)
    createHtml(project_name, destination_folder)
    gCJ(destination_folder)

print('Folders created')
