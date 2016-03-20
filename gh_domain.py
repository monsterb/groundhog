#!/usr/bin/env python3
#
# author:      monsterb (http://monsterb.github.io)
# discription: module for groundhog - Information gathering tool for pentesters.
# email:       UNIX.S3C (at) gmail (dot) com
# filename:    gh_domain.py
# version:     0.00

# Get the top level domain name from the URL:

from tld import get_tld

def get_domain_name(url):
    domain_name = get_tld(url)
    print("Top Level Domain Scan Completed!")
    return domain_name

# Testing 123
#print(get_domain_name(''))
