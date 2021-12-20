# The OS module in Python provides functions for interacting with the operating system.
import os
# The shutil module nables us to operate with file objects easily and without diving into file objects a lot.
import shutil

path = input("Enter Path:  ")
files = os.listdir(path)

for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]
    if os.path.exists(path+ '/'+ extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)

print('Organizing mission completed')

 
