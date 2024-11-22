file_path = "data.txt"

def write_to_file():
    with open(file_path, 'w') as file:
        file.write("This is the first line.\n")
        file.write("This is the second line.\n")
        file.write("This is the third line.\n")
    print("File written successfully.")

def read_from_file():
    with open(file_path, 'r') as file:
        content = file.readlines()
        print("File Content:")
        for line in content:
            print(line.strip())

def update_file():
    with open(file_path, 'a') as file:
        file.write("This is an appended line.\n")
    print("File updated successfully.")

if __name__ == "__main__":
    write_to_file()
    read_from_file()
    update_file()
    read_from_file()