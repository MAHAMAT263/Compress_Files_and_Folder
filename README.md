
README for Compress Folder Script
This script provides a simple and versatile tool for compressing folders with various compression types. The user can choose between 'zip', 'tar', and 'tgz' compression formats. The compressed file will be named based on the original folder's name and the current date.

Prerequisites
Make sure you have Pythoninstalled on your system. This script is compatible with both Python 2 and Python 3.

Usage
Clone the Repository:

bash
Copy code
git clone https://github.com/MAHAMAT263/Compress_file_and_folder
cd your-repo

particiation:
MAHAMAT AHMAT

Run the Script:

bash
Copy code
python compress_folder.py

Enter the Required Information:

Provide the path to the folder you want to compress.
Enter the compression type ('zip', 'tar', or 'tgz'). The input is case-insensitive.

View the Result:

The script will create a compressed file in the same location as the original folder.
The compressed file will be named according to the original folder's name and the current date.

Example
bash
Copy code
Enter the path to the file: /path/to/your/folder
Enter the compress type (zip, tar, tgz): tar
This will create a compressed file named folder_name_day_month_year.tar in the same directory as the original folder.

Supported Compression Types
zip: Compresses the folder using the ZIP format.
tar: Compresses the folder using the TAR format.
tgz: Compresses the folder using the TAR and GZIP formats, creating a '.tar.gz' file.
