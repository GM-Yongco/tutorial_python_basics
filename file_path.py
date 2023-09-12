# Description     : Code that will impress u ;)
# Author          : G.M. Yongco
# HEADER ------------------------------------------------------------------------------------------
import os

def check_if_exist(x:str):
    if not(os.path.exists(x)):
        # need to restart the terminal to update it for some reason
        print(f"Create directory: '{x}'")
        os.mkdir(x)
    else:
        print(f"'{x}' Directory already exists")


print("\nSTART ----------------------------------------\n")

Folder_path_1 = "./REFERENCES"
Folder_path_2 = "./REFERENCES/r_next"

check_if_exist(Folder_path_1)
check_if_exist(Folder_path_2)

print("\nEND ------------------------------------------\n")