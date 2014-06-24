#!/usr/bin/python
import cgi
import cgitb 

from matrix.settings import Settings

from matrix.html.template import template
from matrix.app import errormessage, get_command_content

print "Content-type:text/html\r\n\r\n"
cgitb.enable()


def main():
    settings = Settings('/etc/admin/settings.yaml')

    form = cgi.FieldStorage() 
    if form.getvalue('action'):
        action = form.getvalue('action')
    else: 
        errormessage(message='Page Not Found', reason='The page you requested could not be found, either contact your webmaster or try again.')

    present = False
    for command in settings.system:
        if action == settings.system[command]['id']:
            present = True
            run = command

    if not present:
        errormessage(message='Unknown action', reason='The action you requested has an existential crisis, either read the fucking manual or try again.')
    
    command_output = get_command_content(settings=settings, script=run, page='system')
    body = { 'body': command_output}
    print template % body


main()
