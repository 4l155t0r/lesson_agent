import os

def write_file(working_directory, file_path, content):
    
    working_dir_abs = os.path.abspath(working_directory)
    target_file_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))

    
    valid_target_dir = os.path.commonpath([working_dir_abs, target_file_abs]) == working_dir_abs
    if not valid_target_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    # Check if the target path is a directory
    if os.path.isdir(target_file_abs):
        return f'Error: Cannot write to "{file_path}" as it is a directory'


    try:
        # Create parent directories if they don't exist
        target_dir = os.path.dirname(target_file_abs)
        os.makedirs(target_dir, exist_ok=True)
    except Exception:
        return f'Error: Could not create parent directories for "{file_path}"'
    
    try:
        file = open(target_file_abs, "w")
        file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception:
        return f'Error: Could not write file "{file_path}"'
    
    
    

