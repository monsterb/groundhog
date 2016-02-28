#!/usr/bin/env python3
#
# author:      monsterb (https://www.monsterb.org)
# discription: module for groundhog - Information gathering tool for pentesters.
# email:       unix.s3c (at) gmail (dot) com
# filename:    gh_nmap.py
# version:     0.00

# Let's make some noise:

import os

def get_nmap(options, ip):
    command = "nmap " + options + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return results

# Testing 123
#print(get_nmap('', ''))