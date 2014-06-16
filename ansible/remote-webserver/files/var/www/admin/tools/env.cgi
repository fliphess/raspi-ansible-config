#!/usr/bin/python
import os

print "Content-type: text/html\r\n\r\n";
print "<font size=+1>Environment:</font><br><br>";
for param in os.environ.keys():
    print """<b>%20s</b>: %s<br>\n""" % (param, os.environ[param])
