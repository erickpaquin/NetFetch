#!/usr/bin/env python
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

from datetime import datetime
import sys
import csv
from netmiko import Netmiko

# Verify that the hostfile has been passed to the program, if not exit.
if len(sys.argv) < 2:
    print("You forgot to specify your hosts file?")

# If hostfile has been passed, create a csvreader and start reading lines.
else:
    start_time = datetime.now()
    with open(sys.argv[1]) as csvfile:
        device_read = 0
        hostfile = csv.reader(csvfile)
        hostfile.__next__() # skip the header line.
        for row in hostfile:
            net_connect = Netmiko(
                row[0],
                username=row[1],
                password=row[2],
                secret=row[3],
                device_type=row[4],
                port=row[5],
            )
            net_connect.enable()
            with open(row[6], 'r') as commands:
                for line in commands:
                    line = line.rstrip('\r\n')
                    output = net_connect.send_command(line)
                    filename = row[0] + "_" + line.replace(" ", "_") + ".txt"
                    writefile = open(filename, 'w')
                    writefile.write(output)
                    writefile.close()
            #net_connect.disconnect()
            device_read += 1
            print(device_read, "devices done...")
    print("Process complete.", device_read, "devices read in", str(datetime.now() - start_time), "seconds")
