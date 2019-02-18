########################################################################
# netfetch.py
# 
# This program goes out via ssh or telnet and fetches config
# files of Cisco (and eventually other manufacturers)
# routers and switches.
# 
# Created by Erick Paquin (info@erickpaquin.com)
#
# Version 1.0 (February 17 2019)                                    
# 
############################################################
import argparse  # module to parse command-line arguments to the program.


# Setup the program arguments
argparser = argparse.ArgumentParser()
argparser.parse_args()

