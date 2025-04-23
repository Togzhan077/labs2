#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

if os.path.exists('C:/Users/Admin/Documents/PP_2_labs/LABS/LAB_6/dir_files/asd.txt'):
    os.remove('asd.txt')