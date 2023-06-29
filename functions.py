"""Library of functions for the File renamer"""
import os

def find_music():
    music_files = []
    working_dir = r'C:\\Users\\sjtg1\\Downloads'
    for path in os.listdir(working_dir):
        ext_only = os.path.splitext(path)[1]
        if ext_only == ".mp3":
            print(path)
        else:
            print("No Music")
            break        
def search_filename(filename):
    pass

def print_all_files():
    for file in os.listdir(r'C:\\Users\\sjtg1\\Downloads'):
        print(file)