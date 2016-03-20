#!/usr/bin/env python3
#
# author:      monsterb (http://monsterb.github.io)
# discription: module for groundhog - Information gathering tool for pentesters.
# email:       UNIX.S3C (at) gmail (dot) com
# filename:    gh_whois.py
# version:     0.00

# Good Gravey! You should of paid $10 for that domain name privacy option:

import os

def get_whois(url):
    command = "whois " + url
    process = os.popen(command)
    results = str(process.read())
    print("whois Scan Completed!")
    return results

# Testing 123
#print(get_whois(''))
