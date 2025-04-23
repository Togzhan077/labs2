#Write a Python program to count the number of lines in a text file.
file = open('C:/Users/Admin/Documents/PP_2_labs/LABS/LAB_6/dir_files/alis.txt', 'r')

cnt = 0
for _ in file:
    cnt+=1

print(cnt)