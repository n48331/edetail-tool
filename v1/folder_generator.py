import openpyxl
import shutil

book = openpyxl.load_workbook("./data.xlsx")
data = book.active
project_name = data['A2'].value
source_folder = "./boiler_plate"

# x = f'{project_name}_S{str(1)}_{(data[f"B{2}"].value).replace(" ","_")}'
# print(x)

# for i in range(3):
#     folder_name = f'{project_name}_S{str(i+1)}_{(data[f"B{i+2}"].value).replace(" ","_")}'
#     destination_folder = f"./{project_name}/{folder_name}"
#     shutil.copytree(source_folder, destination_folder)

# print('Folders created')
