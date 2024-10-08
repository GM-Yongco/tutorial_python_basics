# Description     : Code that will impress u ;)
# Author          : G.M. Yongco
# HEADER ------------------------------------------------------------------------------------------
import os
import io

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

# READ -----------------------------------------------------------------

with open(textFile_path_1, 'r') as file:
    # Read the entire contents of the file into a string
    file_contents = file.read()
    print(file_contents)


file_ptr = open(textFile_path_1, "r")
counter = 0
for line in file_ptr:
    print(f"{counter}: {line}" )
    counter = counter +1
file_ptr.close()

# WRITE -----------------------------------------------------------------

f1:io.TextIOWrapper = open(textFile_path_1, "a")
f1.write("\nNow the file has more content!")
print(type(f1))

f1.close()

f2 = open(textFile_path_2, "w")
f2.write("\nNow the file has more content!")
f2.close()
# note: the "a" setting appends; "w" overwrites
# becomes more apparent when this file is ran multiple times

print("the files were written on")



print("\nEND ------------------------------------------\n")