import os

def rename_files(path):
    i = 0
    for filename in os.listdir(path):
        new_model_filename= 'file_' + str(i) + '.txt'
        current_filename = path + filename
        new_name = path + new_model_filename
        os.rename(current_filename, new_name)
        i += 1
    print('Finished!')

def main():
    path = 'C:\\Repos\\Python-Projects\\Rename-Files\\Testes\\'
    rename_files(path)

if __name__ == '__main__': main()
