#!/usr/bin/env python3
#
# author:      monsterb (http://monsterb.github.io)
# discription: module for groundhog - Information gathering tool for pentesters.
# email:       UNIX.S3C (at) gmail (dot) com
# filename:    gh_den.py
# version:     0.00

# Create directories for our files:

import os

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
