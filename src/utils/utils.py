import os

def get_file_name(file_path):
    return os.path.basename(file_path)

def get_project_root():
    return os.path.dirname(os.path.dirname(__file__))

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]

def get_file_path(file_name):
    return os.path.join(get_project_root(), 'data', file_name)

def get_relative_file_path(file_name):
    return os.path.join('..', 'data', file_name)

def check_if_file_exists(file_path):
    return os.path.exists(file_path)

def file_name_without_extension(file_name):
    return os.path.splitext(file_name)[0]