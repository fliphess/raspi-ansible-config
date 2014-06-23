#!/usr/bin/python
import cgi
import cgitb 
from string import Template

from matrix.settings import Settings
from matrix.html.header import header
from matrix.html.modal import modal
from matrix.html.page import page
from matrix.html.sidelinks import sidelinks
from matrix.html.template import template

print "Content-Type: html";

def mainfield(settings):
    body = ''
    for command in sorted(settings.commands):
        data = { 
	       'title': settings.commands[command]['title'],
	       'name': settings.commands[command]['name'],
	       'command': settings.commands[command]['command'],
	       'identifier': settings.commands[command]['id'],
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
    return page % data


cgitb.enable()
settings = Settings('/etc/admin/settings.yaml')
body = { 'body': content(settings=settings)}
print template % body
