# renumberfiles.py

import argparse
import os

def rename(folder):
    dirents=list(filter(os.DirEntry.is_file,os.scandir(folder))) # only files
    dirents.sort(key=lambda e:e.name) # see https://docs.python.org/3/library/os.html#os.scandir
    print(f'found {len(dirents)} files in {folder}')
    print(f'first: {dirents[0].name}')
    print(f' last: {dirents[-1].name}')

def main():
    print('renumber files')
    # get parameters from command line
    parser=argparse.ArgumentParser(description='renumber files')
    parser.add_argument('folder',help='path to folder')
    args=parser.parse_args()
    rename(args.folder)
    print('end.')

if __name__ == '__main__':
    main()

# bug in gopro image file writing, skips round 10k numbers (but every time interval is written)
# e.g.: "Could not open file : photos/G0020000.JPG"
# This code renumbers these files to remove skipped numbers.
