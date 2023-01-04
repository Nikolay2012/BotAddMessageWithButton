'''
    Модуль який створює шлях до файлу 
'''
import os
def path_file(file_name):
    abs_path = __file__
    abs_path = abs_path.split("/")
    del abs_path[-1]
    del abs_path[-1]
    abs_path = "/".join(abs_path)
    abs_path = os.path.join(abs_path, file_name)
    return abs_path
