import os
import shutil

def check_dirs(src, dest):
    if not os.path.exists(src):
        raise ValueError(f"Error: {src} does not exist.")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    copy_files(src, dest)


def copy_files(src, dest):
    file_list = os.listdir(src)
    print(f"Found the following files: {file_list}")
    for file in file_list:
        print("Begining Transfer...")
        file_dir = os.path.join(src, file)
        if os.path.isfile(file_dir):
            print(f"Copying {file} to {dest}")
            shutil.copy(file_dir, dest)
        if os.path.isdir(file_dir):
            new_dir = os.path.join(dest, file)
            print(f"Directory found, creating {new_dir}")
            os.mkdir(new_dir)
            copy_files(file_dir, new_dir)
    print("Transfer Successful!")



