# Rename-Files

This Python script renames all files in a specified folder to a uniform naming pattern: `file_0.txt`, `file_1.txt`, `file_2.txt`, and so on.

## How It Works
The script loops through all files in a specified directory and renames them in a numbered sequence.

### Example
If you have a folder with files:
```
test1.txt
image.png
notes.docx
```
After running the script, they will be renamed to:
```
file_0.txt
file_1.txt
file_2.txt
```

## Project Structure
```
Rename-Files/
├── main.py       # Script to rename files
├── README.md     # Project documentation
└── Testes/       # Example folder with files to rename
    ├── file_0.txt
    ├── file_1.txt
    ├── file_2.txt
    ├── file_3.txt
    └── file_4.txt
```

## How to Use
1. Update the `path` variable in the `main()` function of `main.py` to the folder you want to rename files in.
2. Run the script using the following command:
   ```
   python main.py
   ```

## Important Notes
- Ensure the folder only contains files you want to rename. The script will rename **all files** in the folder.
- The script is designed for Windows paths. Adjust the `path` variable if using another operating system.

## Requirements
- Python 3.x
- No additional libraries are required.