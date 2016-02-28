#!/usr/bin/env python3
#
# author:      monsterb (https://www.monsterb.org)
# discription: groundhog - Information gathering tool for pentesters.
# email:       unix.s3c (at) gmail (dot) com
# filename:    groundhog.py
# version:     0.00

# This is the main executable file for groundhog.

from gh_den import *
from gh_domain import *
from gh_ipaddr import *
from gh_nmap import *
from gh_robots import *
from gh_whois import *

ROOT_DIR = 'targets'
create_dir(ROOT_DIR)


def gather_info(name, url):
    gh_domain = get_domain_name(url)
    gh_ipaddr = get_ip_address(url)
    gh_nmap = get_nmap('-F', gh_ipaddr)
    gh_robots = get_robots_txt(url)
    gh_whois = get_whois(gh_domain)
    create_report(name, url, gh_domain, gh_nmap, gh_robots, gh_whois)
    
    
def create_report(name, full_url, gh_domain, gh_nmap, gh_robots, gh_whois):
    target_dir = ROOT_DIR + '/' + name
    create_dir(target_dir)
    write_file(target_dir + '/full_url.txt', full_url)
    write_file(target_dir + '/top_level_domain.txt', gh_domain)
    write_file(target_dir + '/nmap.txt', gh_nmap)
    write_file(target_dir + '/robots.txt', gh_robots)
    write_file(target_dir + '/whois.txt', gh_whois)
    
#gather_info('folder name goes here', 'url goes here')

    