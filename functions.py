"""
Library/Module name: Functions

Author: Sam Goldberg
"""



import os
    
def find_music():
    """ Searches for music files using extensions listed in an array. 
    """
    mus_ext = ['.mp3', '.wav', '.aac', '.m4a']
    working_dir = r'C:\\Users\\sjtg1\\Downloads'
    for path in os.listdir(working_dir):
        ext_only = os.path.splitext(path)[1]
        for mext in mus_ext:
            if ext_only == mext: #Adding else statement messes up the MP3 search!
                print(os.path.join(path, ext_only))       
def search_filename(filename):
    """Searches for file name in directory

    Args:
        filename (obj): the name of the file to search for
    """
    pass

def print_all_files():
    for file in os.listdir(r'C:\\Users\\sjtg1\\Downloads'):
        print(file)