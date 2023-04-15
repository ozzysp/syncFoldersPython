# ****************************************************************************
# *  This script was created by:                                             *
# *  Ozzy -  https://github.com/ozzysp/syncFoldersPython                     *
# *  Date   :  2021-04-01                                                    *
# *  Version:  1.0.0                                                         *
# *  License:  GNU                                                           *
# ****************************************************************************

import os
import shutil
import datetime
import hashlib
import time

def get_user_input():
    source_dir_path = input("Enter the path to the source directory: ")
    replica_dir_path = input("Enter the path to the replica directory: ")
    log_dir_path = input("Enter the path to the log directory: ")
    interval = int(input("Enter the interval of time for synchronization routine (in minutes): "))
    return source_dir_path, replica_dir_path, log_dir_path, interval


def check_and_clear_replica(replica_dir_path):
    if os.path.exists(replica_dir_path) and os.path.isdir(replica_dir_path):
        if os.listdir(replica_dir_path):
            shutil.rmtree(replica_dir_path)
            print(f"Deleted all content from {replica_dir_path}")
        else:
            print(f"{replica_dir_path} is already empty")
    else:
        print(f"{replica_dir_path} does not exist or is not a directory")


def synchronize_directories(source_dir_path, replica_dir_path, log_dir_path):
    check_and_clear_replica(replica_dir_path)
    shutil.copytree(source_dir_path, replica_dir_path)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    num_files = sum(len(files) for _, _, files in os.walk(source_dir_path))
    log_file_path = os.path.join(log_dir_path, "log.txt")

    with open(log_file_path, "a") as log_file:
        log_file.write(f"{timestamp} - Copied {num_files} files from {source_dir_path} to {replica_dir_path}\n")

    print(f"Synchronized {source_dir_path} and {replica_dir_path}. Backup logged to {log_file_path}")


def compare_directories(source_dir_path, replica_dir_path):
    for root, dirs, files in os.walk(source_dir_path):
        for file in files:
            source_file_path = os.path.join(root, file)
            replica_file_path = os.path.join(replica_dir_path, os.path.relpath(source_file_path, source_dir_path))

            source_file_hash = hashlib.md5()
            with open(source_file_path, "rb") as source_file:
                for chunk in iter(lambda: source_file.read(4096), b""):
                    source_file_hash.update(chunk)
            source_file_md5 = source_file_hash.hexdigest()

            replica_file_hash = hashlib.md5()
            with open(replica_file_path, "rb") as replica_file:
                for chunk in iter(lambda: replica_file.read(4096), b""):
                    replica_file_hash.update(chunk)
            replica_file_md5 = replica_file_hash.hexdigest()

            if source_file_md5 != replica_file_md5:
                print(f"File {os.path.relpath(source_file_path, source_dir_path)} is corrupted")
                return False
    print("Copies made and verified with success")
    return True


def run_backup_routine(source_dir_path, replica_dir_path, log_dir_path, interval):
    while True:
        synchronize_directories(source_dir_path, replica_dir_path, log_dir_path)
        compare_directories(source_dir_path, replica_dir_path)
        time.sleep(interval * 60)

source_dir_path, replica_dir_path, log_dir_path, interval = get_user_input()
synchronize_directories(source_dir_path, replica_dir_path, log_dir_path)
compare_directories(source_dir_path, replica_dir_path)
run_backup_routine(source_dir_path, replica_dir_path, log_dir_path, interval)