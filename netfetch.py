########################################################################
# netfetch.py
#
# THIS program goes out via ssh or telnet and fetches config
# files of Cisco (and eventually other manufacturers)
# routers and switches.
#
# Created by Erick Paquin, info@erickpaquin.com
#
# Version 1.0 (last updated March 21 2019)
#
############################################################

import fileinput
import telnetlib
import netmiko

for line in fileinput.input():
        print(line)

