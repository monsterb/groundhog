#!/usr/bin/env python3

# author:      monsterb (https://www.monsterb.org)
# discription: module for groundhog - Information gathering tool for pentesters.
# email:       unix.s3c (at) gmail (dot) com
# filename:    gh_den.py
# version:     0.00

import os

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedir(directory)
        
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()