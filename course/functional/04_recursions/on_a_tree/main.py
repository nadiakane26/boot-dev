def list_files(parent_directory, current_filepath=""):
    """
    parent_directory: A dictionary of dictionaries representing the current directory. A child directory's value is a dictionary and a file's value is None.
    current_filepath: A string representing the current path (e.g. /dir1/dir2/filename.txt)
    """ 
    files = []
    for key, value in parent_directory.items():
        new_file_path = current_filepath + "/" + key 
        if value is None:
            files.append(new_file_path)
        else:
            files.extend(list_files(value, new_file_path)) 
    return files