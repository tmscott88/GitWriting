import os
import app_utils as app

def get_entries_in_directory(path, include_hidden=False):
    """(Python 3.5+) Return an array of DirEntry object names corresponding to the entries in the given directory."""
    results = []
    for entry in os.scandir(path):
        if not include_hidden:
            if not entry.name.startswith('.'):
                results.append(entry.name)
        else:
            results.append(entry.name)
    return results

def get_folders_in_directory(path, include_hidden=False):
    """Return an list of names corresponding to the (folder) entries in the given directory. (DIRECTORIES ONLY)"""
    results = []
    for entry in os.scandir(path):
        if not include_hidden:
            if not entry.name.startswith('.') and entry.is_dir():
                results.append(entry.name)
        else:
            if entry.is_dir():
                results.append(entry.name)
    return results

def get_path_head(path):
    """Returns one directory higher than the specified path."""
    head, _ = os.path.split(path)
    return head

def get_path_tail(path):
    """Returns the last part of the path"""
    _, tail = os.path.split(path)
    return tail

def create_new_file(new_path):
    """Creates a new file if needed."""
    if not is_file(new_path) and not is_directory(new_path):
        try:
            # Only make new directory/directories if the file path forms a directory.
            if os.path.dirname(new_path) != "":
                os.makedirs(os.path.dirname(new_path), exist_ok=True)
            with open(new_path, 'w', encoding="utf-8"):
                app.print_success(f"Created file '{new_path}'")
        except OSError as e:
            app.print_error(f"Failed to create file '{new_path}'. {e}")
    elif not is_file(new_path) and is_directory(new_path):
        app.print_error(f"A folder '{new_path}' already exists in this directory. Please create a different file name or directory.")

def create_new_directory(new_path):
    """Creates a new directory (and any intermediate directories denoted by the path seperator) if needed."""
    if not is_directory(new_path) and not is_file(new_path):
        try:
            # TODO test path normalization
            os.makedirs(new_path, exist_ok=True)
            app.print_success(f"Created new directory '{new_path}'")
        # Shouldn't reach this since exist_ok=True but keep it just in case
        except FileExistsError as e:
            app.print_error(f"Failed to create directory '{new_path}'. {e}")
    elif not is_directory(new_path) and is_file(new_path):
        app.print_error(f"A file '{new_path}' already exists in this directory. Please create a different directory name.")
        raise FileExistsError

def is_file(path):
    return bool(os.path.isfile(path))
    
def is_directory(path):
    return bool(os.path.isdir(path))
