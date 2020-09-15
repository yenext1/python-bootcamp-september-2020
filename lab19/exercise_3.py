# get pc name via command line and return ip according hosts file
import sys

names = sys.argv
hosts_data = {}
with open('hosts', 'r', encoding='UTF-8') as f:
    for line in f:
        line = line.split('=')
        hosts_data[line[0]] = line[1].rstrip()

for name in names[1:]:
    try:
        print(f"{name} IP address is {hosts_data[name]}")
    except KeyError:
        print(f"{name} is not in hosts file")

"""
Uri's comments:
==============

* Very good! This code works.
* It's better to put your data files in a separate folder and not with
  the code.

"""
