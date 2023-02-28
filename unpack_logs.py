import glob
from zipfile import ZipFile
import os
import sys
import re


def unzip_grizzly_logs():
    print("Extracting grizzly logs...")
    for file_name in glob.glob("grizzly.log.*.zip"):
        # opening the zip file in READ mode
        with ZipFile(file_name, 'r') as zip:
            zip.extractall()
        os.remove(file_name)

def rename_log_files():
    print("Renaming log files...")
    # Sort the unzipped files that contain the timestamp, so that the newest ones are on top.
    UNZIPPED_FILES = reversed((sorted(glob.glob("grizzly.log.*.txt"))))
    #Rename the log file from the timestamp into something more friendly, such as grizzly.log.01.txt
    count = 1
    for file in UNZIPPED_FILES:
        os.rename(file, "grizzly.log.0" + str(count) + ".txt")
        count += 1

# Find all instance logs and unzip them to their own directory and delete their zip files.
def unzip_instance_logs():
    zipped_dir = None
    unzipped_dir = None
    for file in os.listdir():
        if file.startswith("logs_") and file.endswith(".zip"):
            zipped_dir = file

    with ZipFile(zipped_dir, "r") as zip:
        zip.extractall()
    
    unzipped_dir = zipped_dir.replace(".zip", "")

    for file in os.listdir(unzipped_dir):
        with ZipFile(file, "r") as zip:
            zip.extractall(file + "_extracted")
        os.remove(file)
    

def unzip_db_dump():
    print("Extracting db_dump...")
    with ZipFile("db_dump.zip", 'r') as db_zip:
        db_zip.extractall("db_dump")

def concatenate_log_files():
    print("Merging log files...")
    read_files = glob.glob("grizzly.log.*")
    with open("aggregated_logs.txt", "wb") as outfile:
        for f in reversed(read_files):
            with open(f, "rb") as infile:
                outfile.write("START OF ".encode("utf-8") + f.encode("utf-8") + "\n".encode("utf-8"))
                outfile.write(infile.read())


if __name__ == "__main__":
    unzip_grizzly_logs()
    rename_log_files()
    '''
    unzip_instance_logs()
    unzip_db_dump()
    '''
    if "-concat" in sys.argv:
        concatenate_log_files()
    print("DONE!")



