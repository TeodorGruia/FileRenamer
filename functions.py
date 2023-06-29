"""Library of functions for the File renamer"""
import os

def find_music():
    mus_ext = ['.mp3', '.wav', '.aac', '.m4a']
    working_dir = r'C:\\Users\\sjtg1\\Downloads'
    for path in os.listdir(working_dir):
        ext_only = os.path.splitext(path)[1]
        for mext in mus_ext:
            if ext_only == mext:
                print(os.path.join(path, ext_only))       
def search_filename(filename):
    pass

def print_all_files():
    for file in os.listdir(r'C:\\Users\\sjtg1\\Downloads'):
        print(file)