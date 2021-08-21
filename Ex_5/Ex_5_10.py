from os.path import join,isfile,isdir
from os import listdir,getlogin

##list all folders in C:\windows directory
file_path = "C:\\Windows"
folder_list = [f for f in listdir(file_path) if isdir(join(file_path,f))]
print('Folders of windows directory:')
print(folder_list)

#####
print()
print()
#####


##list all files in C:\windows directory
file_list = [f for f in listdir(file_path) if isfile(join(file_path,f))]
print('Files of windows directory:')
print(file_list)

#####
print()
print()
#####




##using getlogin method to access desktop directory
user = getlogin()
dirctory  = "C:\\Users"
#desktop folders
desktop_folder = [f for f in listdir(join(dirctory,user,'Desktop')) if isdir(join(dirctory,user,'Desktop',f))]
print('Folders of desktop directory:')
print(desktop_folder)

print()

#desktop files
desktop_file = [f for f in listdir(join(dirctory,user,'Desktop')) if isfile(join(dirctory,user,'Desktop',f))]
print('Files of desktop directory:')
print(desktop_file)


