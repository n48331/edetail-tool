import os
import shutil

n = 3
folder_name = "1234_AB"
source_folder = "./files"

for i in range(n):
    name = folder_name + "_S"+str(i+1)
    destination_folder = f"./folders/{name}"
    shutil.copytree(source_folder, destination_folder)
    os.rename(f"./folders/{name}/full.jpg",
              f"./folders/{name}/{name}-full.jpg")
    os.rename(f"./folders/{name}/thumb.jpg",
              f"./folders/{name}/{name}-thumb.jpg")
    os.rename(f"./folders/{name}/index.html",
              f"./folders/{name}/{name}.html")

print("Directory created")
