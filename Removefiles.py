import os
import time
import shutil

def main():
    deleted_folders=0
    deleted_files=0
    path="E:/backup for windows 10/cats"
    days=7
    seconds=time.time()-(days*24*60*60)
    
    if os.path.exists(path):
        for main_folder,subfolders,files in os.walk(path):
            if seconds>=getctime(main_folder):
                remove_folder(main_folder)
                deleted_folders+=1
                break
            else:
                for folder in subfolders:
                    folder_path=os.path.join(main_folder,folder)
                    if seconds>=getctime(folder_path):
                        remove_folder(folder_path)
                        deleted_folders+=1

                for file in files:
                    file_path=os.path.join(main_folder,file)
                    if seconds>=getctime(file_path):
                        remove_file(file_path)
                        deleted_files+=1

        else:
            if seconds>=getctime(path):
                remove_file(path)
                deleted_files+=1
    else:
        print('Path not found!')

    print('Total Folder deleted: ',deleted_folders)
    print('Total files deleted: ',deleted_files)    


                

def getctime(path):
    ctime=os.stat(path).st_ctime
    return ctime

def remove_folder(path):
    if not shutil.rmtree(path):
        print('Succefully Removed!')
    else:
        print('Enable to delete the path!')  

def remove_file(path):
    if not os.remove(path):
        print('Succefully Removed!')
    else:
        print('Enable to delete the file!')

main()