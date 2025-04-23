#Write a Python program to copy the contents of a file to another file
import os
import shutil

def copy(f1, f2):
    if os.path.isfile(f1):
        shutil.copyfile(f1, f2)
        print('copied')
    else:
        print('file doesnt exists')
    
f1 = 'C:/Users/Admin/Documents/PP_2_labs/LABS/LAB_6/dir_files/7text.txt'
f2 = 'C:/Users/Admin/Documents/PP_2_labs/LABS/LAB_6/dir_files/7text_copyy.txt'
copy(f1, f2)