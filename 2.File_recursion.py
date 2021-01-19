import os

def find_files(suffix, path):

    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if not os.path.isdir(path):
        return "The path doesn't exist"

    all_items = os.listdir(path)
    sub_dirs = []
    files_with_suffix = []

    for i in all_items:
        item = os.path.join(path, i)
        if os.path.isfile(item) and item.endswith(suffix):
            files_with_suffix.append(item)
        elif os.path.isdir(item):
            sub_dirs.append(item)

    for i in sub_dirs:
        files_with_suffix = files_with_suffix + find_files(suffix, i)

    return files_with_suffix


# test cases
print(find_files('c', './testdir'))
print(find_files('', './testdir')) #edge case, empty string input, it should return all the files.
print(find_files('happy', './testdir')) #edge case, string input that doesn't exist in the folder

