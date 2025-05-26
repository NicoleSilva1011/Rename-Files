# Rename-Files
This Python script renames all files in a specified folder to a uniform naming pattern: file_0.txt, file_1.txt, file_2.txt, and so on. 

How It Works
The script loops through all files in a specified directory and renames them in a numbered sequence.

Example
If you have a folder with files:
test1.txt  
image.png  
notes.docx  
After running the script, they will be renamed to:

file_0.txt  
file_1.txt  
file_2.txt  
How to Use
Update the path variable in the main() function to the folder you want to rename files in.

Run the script using:
python rename_files.py

Important
Make sure the folder only contains files you want to rename. The script will rename all files in the folder.