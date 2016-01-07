# Author		: Pranjal Dubey
# Created		: 07 Jan 2016
# Last Modified	:
# Version		: 1.0
# Modifications	:
# Description	: script to find and delete all Thumbs.db files
# Known Bugs    :

#importing vendor modules
import os, sys

if len(sys.argv) > 1:
    dirname = sys.argv[1]

    for dirname, subdirs, filenames in os.walk(dirname):
        for filename in filenames:
            print(filename)
