def compare_files(file1, file2):
    try:
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
            content1 = f1.read()
            content2 = f2.read()
            
            if content1 == content2:
                print("The files are identical.")
            else:
                print("The files are different.")
    except FileNotFoundError:
        print("One or both files do not exist. Please check the file names.")

# Get file names from the user
file1 = input("Enter the first file name: ")
file2 = input("Enter the second file name: ")

compare_files(file1, file2)
