import os


def get_input_path(script_file, input_file_name):
    script_dir = os.path.dirname(script_file)
    input_folder = os.path.join(script_dir, 'input_files')
    return os.path.join(input_folder, input_file_name)