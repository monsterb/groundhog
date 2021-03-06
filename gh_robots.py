#!/usr/bin/env python3
#
# author:      monsterb (http://monsterb.github.io)
# discription: module for groundhog - Information gathering tool for pentesters.
# email:       UNIX.S3C (at) gmail (dot) com
# filename:    gh_robots.py
# version:     0.00

# Dear Robot, Show me your masters secret files:

import urllib.request
import io

def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib.request.urlopen(path + "robots.txt", data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')
    print("robots.txt Scan Completed!")
    return data.read()

# Testing 123
#print(get_robots_txt(''))


