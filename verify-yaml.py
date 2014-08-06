#!/usr/bin/env python
import os
import sys
import yaml

def usage():
    print "Usage: %s filename" % sys.argv[0]
    sys.exit(1)

if len(sys.argv) != 2: 
    usage()

filename = sys.argv[1]
if not os.path.isfile(filename):
    print "File %s does not exists!" % filename
    sys.exit(1)

with open(filename) as fh:
    try:
        c = yaml.load(fh)
    except Exception as e:
        print "Failed to load %s! Error was: %s" % (filename, e)
        sys.exit(1)
    print "%s seems to be a proper yaml file!" % filename
