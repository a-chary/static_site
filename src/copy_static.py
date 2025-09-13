import os
import shutil
import sys

from config import DEST, SOURCE

def delete_files(dir):

    if not os.path.isdir(dir):
        print("Error, directory does not exist")
        sys.exit(1)
            
    shutil.rmtree(dir)
    return


def copy_directory_files(src, dest):
    
    if not os.path.isdir(src):
        print("Error, source directory does not exist")
        sys.exit(1)
    
    if not os.path.isdir(dest):
        os.mkdir(dest)

    source_files = os.listdir(src)
    for file in source_files:
        f_path = os.path.join(src, file)
        d_path = os.path.join(dest, file)
        if os.path.isfile(f_path):
            shutil.copy(f_path, d_path)
        elif os.path.isdir(f_path):
            copy_directory_files(f_path, d_path)
    
    return


def copy_files():
    src_path = os.path.abspath(SOURCE)
    dest_path = os.path.abspath(DEST)
    delete_files(dest_path)
    copy_directory_files(src_path, dest_path)
    return