import os
import shutil

n = 3
folder_name = "1234_AB"
source_folder = "./files"
key_message = "_S"

for i in range(n):
    name = folder_name + key_message+str(i+1)
    destination_folder = f"./{folder_name}/{name}"
    shutil.copytree(source_folder, destination_folder)
    os.rename(f"{destination_folder}/full.jpg",
              f"{destination_folder}/{name}-full.jpg")
    os.rename(f"{destination_folder}/thumb.jpg",
              f"{destination_folder}/{name}-thumb.jpg")
    os.rename(f"{destination_folder}/index.html",
              f"{destination_folder}/{name}.html")

print("Directory created")
