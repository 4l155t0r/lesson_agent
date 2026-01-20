import os

def get_files_info(working_dir, directory):
    # Get the absolute path of the script's parent directory (08_Agent)
    #working_dir_abs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    working_dir_abs = os.path.abspath(working_dir)
    target_dir_abs = os.path.normpath(os.path.join(working_dir_abs, directory))

    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir_abs]) == working_dir_abs

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    # Check if the target path is a directory
    if not os.path.isdir(target_dir_abs):
        return f'Error: "{directory}" is not a directory'

    try:
        for item in os.listdir(target_dir_abs):
            item_path = os.path.join(target_dir_abs, item)

            size = os.path.getsize(item_path)
            if os.path.isdir(item_path):
                is_dir = True
            else:
                is_dir = False

            row_to_print = f"{item}: file_size={size} bytes, is_dir={is_dir}"
            print(row_to_print)
    except Exception as e:
        return "Error: could not iterate over the items in the directory."
    
    return 0

if __name__ == "__main__":
    import sys
    working_dir = sys.argv[1]
    directory = sys.argv[2]
    get_files_info(working_dir, directory)
