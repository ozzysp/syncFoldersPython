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


source_dir_path, replica_dir_path, log_dir_path, interval = get_user_input()
