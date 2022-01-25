# The OS module in Python provides functions for interacting with the operating system.
import os
# The shutil module nables us to operate with file objects easily and without diving into file objects a lot.
import shutil

# Input path of the place you want to organize and open the files
path = input("Enter Path:  ")
files = os.listdir(path)

for file in files:
    # Divide each files into filename and extension
    filename,extension = os.path.splitext(file)
    extension = extension[1:]
    # Check if files of extension exist or not
    if os.path.exists(path+ '/'+ extension):
        # if exists, move the file to that files of extension
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        # if doen't exists, add a new file of extension and then move files into it
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)

print('Organizing mission completed')

 
