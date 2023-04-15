# ****************************************************************************
# *  This script was created by:                                             *
# *  Ozzy -  https://github.com/ozzysp/syncFoldersPython                     *
# *  Date   :  2021-04-01                                                    *
# *  Version:  1.0.0                                                         *
# *  License:  GNU                                                           *
# ****************************************************************************


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


source_dir_path, replica_dir_path, log_dir_path, interval = get_user_input()
check_and_clear_replica(replica_dir_path)
