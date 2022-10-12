import os.path

path = input("Enter a file to read : ")

if os.path.exists(path):
    file = open(path, "r")
    file_content = ""
    try:
        file_content = file.read()
    except UnicodeDecodeError:
        print("Cannot read this file format.")
    finally:
        print(file_content)
        file.close()
else:
    print("This file does not exist.")
