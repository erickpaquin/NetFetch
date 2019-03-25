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

import threading
from datetime import datetime
import sys
import csv
from epaquinlib import get_devices

# Verify that the hostfile has been passed to the program, if not exit.
if len(sys.argv) < 2:
    print("You forgot to specify your hosts file?")

# If hostfile has been passed, create a csvreader and start reading lines.
else:
    start_time = datetime.now()
    device_read = 0
    with open(sys.argv[1]) as csvfile:
        hostfile = csv.reader(csvfile)
        hostfile.__next__() # skip the header line.
        for row in hostfile:
            my_thread = threading.Thread(target=get_devices, args=(row,))
            my_thread.start()
    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            device_read += 1
            some_thread.join()
    print("Process complete.", device_read, "devices read in", str(datetime.now() - start_time), "seconds")
