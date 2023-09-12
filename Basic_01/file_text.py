# Description     : Code that will impress u ;)
# Author          : G.M. Yongco
# HEADER ------------------------------------------------------------------------------------------
import os

def check_if_exist(x:str):
    if not(os.path.exists(x)):
        print(f"Create directory: '{x}'")
        os.mkdir(x)
    else:
        print(f"'{x}' Directory already exists")

print("\nSTART ----------------------------------------\n")
   
# Check whether the specified path exists or not
# create path if not

Folder_path = "./REFERENCES"
textFile_path_1 = "./REFERENCES/example_txt_1.txt"
textFile_path_2 = "./REFERENCES/example_txt_2.txt"

# CREATE -----------------------------------------------------------------

check_if_exist(Folder_path)

try:
    f1 = open(textFile_path_1, "x")
    f2 = open(textFile_path_2, "x")
    f1.close()
    f2.close()
except Exception as error:
    print("An exception occurred:", error)

# open for exclusive creation and fails if file exists
# closing files after use is good practice  

# WRITE -----------------------------------------------------------------

f1 = open(textFile_path_1, "a")
f1.write("\nNow the file has more content!")
f1.close()

f2 = open(textFile_path_2, "w")
f2.write("\nNow the file has more content!")
f2.close()
# note: the "a" setting appends; "w" overwrites
# becomes more apparent when this file is ran multiple times

print("the files were written on")

print("\nEND ------------------------------------------\n")