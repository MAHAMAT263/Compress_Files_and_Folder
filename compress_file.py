#!/usr/bin/python3
#import the modules
import shutil
import tarfile
import os
import datetime

#define a function
def compress_folder(path_to_folder, compress_type):
    #create a variable that is equal to the folder_name
    folder_name = os.path.basename(path_to_folder)
    # the time of creation variable
    current_date = datetime.datetime.now().strftime("%d_%m_%Y")
    # to define the name of the compressed file eg:(Myfolder_08_02_2024)
    compressed_filename = f"{folder_name}_{current_date}"
    """ here are the conditions that allow the user to choose an specifique compress_type """
    if compress_type == 'zip':
        shutil.make_archive(compressed_filename, 'zip', path_to_folder)
    elif compress_type == 'tar':
        shutil.make_archive(compressed_filename, 'tar', path_to_folder)
    elif compress_type == 'bz2' :
        bz2.add()
    elif compress_type == 'tgz':
        with tarfile.open(f"{compressed_filename}.tar.gz", "w:gz") as tar:
            tar.add(path_to_folder, arcname=os.path.basename(path_to_folder))
     # the confirmations messages when the process is successful done
    print(f"Compression successful. File saved as {compressed_filename}.{compress_type}")
"""the inputs that allow the users to enter the folder_path_name and
the type of compress(which will transform the uppercase to a lowercase if entered by the users)"""
path_to_folder = input('enter the path to the file: ')
compress_type = input("Enter the compress type (zip, tar, tgz): ").lower()

compress_folder(path_to_folder, compress_type)
