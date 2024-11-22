import os

def rename_file(directory, index):
    for filename in os.listdir(directory):
        old_filepath = os.path.join(directory,filename)
        new_filename=f"photo_{index}.jpg"
        new_filepath = os.path.join(directory,new_filename)
        os.rename(old_filepath,new_filepath)
        index += 1

directory_path  = "."
index = 1
rename_file(directory_path,index)