"""
Rename music files without the crap that Youtube downloaders add
"""
import os

def main():
    print_all_files()

def find_music():
    music_files = []
    working_dir = r'C:\\Users\\sjtg1\\Downloads'
    for path in os.listdir(working_dir):
        if path.endswith(".mp3") == True:
            print(path)
        else:
            print("No Music!")
            break
        
def search_filename(filename):
    pass

def print_all_files():
    for file in os.listdir(r'C:\\Users\\sjtg1\\Downloads'):
        print(file)

if __name__ == '__main__': main()
