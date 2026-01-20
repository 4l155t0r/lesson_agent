
import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    
    working_dir_abs = os.path.abspath(working_directory)
    target_file_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))

    
    valid_target_dir = os.path.commonpath([working_dir_abs, target_file_abs]) == working_dir_abs
    if not valid_target_dir:
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    # Check if the target path is a file
    if not os.path.isfile(target_file_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        file = open(target_file_abs, "r")
        content = file.read(10000)
        # After reading the first MAX_CHARS...
        if file.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content
    except Exception:
        return f'Error: Could not read file: "{file_path}"'