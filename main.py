#****************************************************************************
#*  This script was created by:                                             *
#*  Ozzy -  https://github.com/ozzysp/syncFoldersPython                     *
#*  Date   :  2021-04-01                                                    *
#*  Version:  1.0.0                                                         *
#*  License:  MIT                                                           *
#****************************************************************************

def get_paths():
    source_dir = input("Enter the source folder path: ")
    replica_dir = input("Enter the destin folder path: ")
    return source_dir, replica_dir


def get_interval():
    interval = input("Enter the sync interval (in hours): ")
    return int(interval)


def get_log_path():
    log_path = input("Enter the log file path: ")
    return log_path
