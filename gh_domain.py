#!/usr/bin/env python3

# author:      monsterb (https://www.monsterb.org)
# discription: module for groundhog - Information gathering tool for pentesters.
# email:       unix.s3c (at) gmail (dot) com
# filename:    gh_domain.py
# version:     0.00

# To get the top level domain name from the URL given:

from tld import get_tld

def get_domain_name(url):
    domain_name = get_tld(url)
    return domain_name

# Testing 123
#print(get_domain_name(''))