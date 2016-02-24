#!/usr/bin/env python3

# author:      monsterb (https://www.monsterb.org)
# discription: module for groundhog - Information gathering tool for pentesters.
# email:       unix.s3c (at) gmail (dot) com
# filename:    gh_ipaddr.py
# version:     0.00

import os

def get_ip_address(url):
    command = 'host ' + url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address') + 12
    return results[marker:].splitlines()[0]

# Testing 123
#print(get_ip_address('oggcastplanet.org'))
