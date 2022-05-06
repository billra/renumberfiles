# renumberfiles.py

import argparse
import os

def number_from_filename(name):
    part=name[1:-4] # specific to gopro image numbering
    return int(part)

def filename_from_number(number):
    return f'G{number:07d}.JPG'

def rename(folder):
    dirents=list(filter(os.DirEntry.is_file,os.scandir(folder))) # only files
    dirents.sort(key=lambda e:e.name) # see https://docs.python.org/3/library/os.html#os.scandir
    print(f'found {len(dirents)} files in {folder}')
    print(f'first: {dirents[0].name}')
    print(f' last: {dirents[-1].name}')
    expect_num=number_from_filename(dirents[0].name) # expected number in filename
    offset=0
    for dirent in dirents:
        current_num=number_from_filename(dirent.name)
        if current_num!=expect_num:
            offset+=current_num-expect_num
            print(f'missing {expect_num}, got {current_num}, offset is now {offset}')
        if offset: # do a rename
            pass # todo
        expect_num=current_num+1
        print(filename_from_number(current_num))

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
