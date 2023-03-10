import shutil
import os

def find_original_tsv_file():
    tsv_file_name = None
    for file in os.listdir():
        if file.startswith("target.tsv_"):
            tsv_file_name = file
    return tsv_file_name


def make_files(tsv_name):
    tsv_file_number = tsv_name.split("_")[1]
    for i in range(1, 1001):
        # create new file name by incrementing number
        new_filename = "target.tsv_" + str(int(tsv_file_number) + i)
        # copy original file to new file name
        shutil.copyfile(tsv_name, new_filename)
        # print confirmation message for each file copied
        print(f"Copied {tsv_name} to {new_filename}")
    return

if __name__ == "__main__":
    tsv_file_name = find_original_tsv_file()
    print("Original file: " + tsv_file_name)
    make_files(tsv_file_name)