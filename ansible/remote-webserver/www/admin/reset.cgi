#!/usr/bin/python
import cgitb 

from matrix.settings import Settings
from matrix.html.modal import modal
from matrix.html.reset import indexpage
from matrix.html.sidelinks import sidelinks
from matrix.html.template import template

print "Content-Type: html";

def mainfield(settings):
    body = ''
    for command in sorted(settings.system):
        data = { 
	       'title': settings.system[command]['title'],
	       'name': settings.system[command]['name'],
	       'command': settings.system[command]['command'],
	       'identifier': settings.system[command]['id'],
	       'postscript': '/admin/system.cgi',
	       'tag': command,
        }
        body += modal % data
    return body


def sidefield(settings):
    body = ''
    for link in sorted(settings.links):
        body += sidelinks % (settings.links[link]['link'], settings.links[link]['name'].title())
    return body


def content(settings):
    data = { 'mainfield': mainfield(settings), 'sidefield': sidefield(settings)}
    return indexpage % data


cgitb.enable()
settings = Settings('/etc/admin/settings.yaml')
body = {'body': content(settings=settings)}
print template % body
