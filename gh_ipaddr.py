#!/usr/bin/env python3
#
# author:      monsterb (http://monsterb.github.io)
# discription: module for groundhog - Information gathering tool for pentesters.
# email:       UNIX.S3C (at) gmail (dot) com
# filename:    gh_ipaddr.py
# version:     0.00

# Get just the ip address from host:

import os

def get_ip_address(url):
    command = 'host ' + url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address') + 12
    print("IP Address Completed!")
    return results[marker:].splitlines()[0]

# Testing 123
#print(get_ip_address(''))
