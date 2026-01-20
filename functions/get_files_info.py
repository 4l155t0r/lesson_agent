import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def get_files_info(working_directory, directory=""):
    # Get the absolute path of the script's parent directory (08_Agent)
    #working_dir_abs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    working_dir_abs = os.path.abspath(working_directory)
    target_dir_abs = os.path.normpath(os.path.join(working_dir_abs, directory))

    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir_abs]) == working_dir_abs

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    # Check if the target path is a directory
    if not os.path.isdir(target_dir_abs):
        return f'Error: "{directory}" is not a directory'

    try:
        content = ""
        for item in os.listdir(target_dir_abs):
            item_path = os.path.join(target_dir_abs, item)

            size = os.path.getsize(item_path)
            if os.path.isdir(item_path):
                is_dir = True
            else:
                is_dir = False

            row_to_print = f"{item}: file_size={size} bytes, is_dir={is_dir}"
            content += row_to_print + "\n"
        return content.strip()
    except Exception as e:
        return "Error: could not iterate over the items in the directory."
    
    return 0

if __name__ == "__main__":
    import sys
    working_dir = sys.argv[1]
    directory = sys.argv[2]
    get_files_info(working_dir, directory)
