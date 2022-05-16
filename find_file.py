import os
import stat


def get_executable_file(directory_path):
    """
    This function returns the full path of the first file inside a given directory that that meets the following
    requirements:
        a. The file owner is admin
        b. The file is executable
        c. The file has a size lower than 14*2^20
    :param directory_path: the path of the directory to find the file
    :return: the full path of the file that meets the conditions described before
    :raises: NotADirectoryError if the argument directory_path does not correspond with a valid directory path
             FileNotFoundError if the argument directory_path does not correspond with an existing directory
    """
    try:
        path_content = os.listdir(directory_path)
        for file in path_content:
            full_path = os.path.join(directory_path, file)
            if os.path.isfile(full_path):
                size = os.stat(full_path).st_size
                executable_file = is_executable(full_path)
                owner = os.stat(full_path).st_gid
                if executable_file and owner == 0 and size < 14*2**20:
                    return full_path
        return None
    except NotADirectoryError as e:
        raise e
    except FileNotFoundError as e1:
        raise e1


def is_executable(filename):
    """
    This function checks if a file is an executable file
    :param filename: the file to be evaluated
    :return: True is the file is an executable file
             False if not
    """
    executable = stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH
    if os.path.isfile(filename):
        st = os.stat(filename)
        mode = st.st_mode
        if mode & executable:
            return True
    return False
