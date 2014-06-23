#!/usr/bin/python
import cgi
import cgitb 
import sys
import subprocess

from matrix.settings import Settings

from matrix.html.error import error
from matrix.html.template import template
from matrix.html.template import codefield
from matrix.html.template import alert_ok, alert_nok
from matrix.html.template import input_page, return_footer

def errormessage(message, reason):
    errormsg = { 'message': message, 'reason': reason}
    content = error % errormsg
    errorpage = { 'body': content}
    print template % errorpage
    sys.exit(0)


def run_command(script):
    output = []
    script += ' 2>&1'
    process = subprocess.Popen(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        nextline = process.stdout.readline()
        if nextline == '' and process.poll() != None:
            break
        elif nextline == '\n' or nextline == '':
            continue
        output.append(nextline)
    exitcode = process.returncode
    return output, exitcode


def get_command_content(settings, script):
    body = ''
    html_escape_table = { '"': "&quot;", "'": "&apos;", "&": "&amp;", ">": "&gt;", "<": "&lt;"}
    execute = settings.commands[script]['command']
    output, exitcode = run_command(execute)
    data = {'output': output, 'command': script, 'exitcode': exitcode}
    if exitcode != 0:
	    body += input_page % {'content': alert_nok % data}
    else:
	body += input_page % {'content': alert_ok % data}
    
    output_block = ''
    for line in output:
        output_block += line

    codeblock_content = cgi.escape(output_block, False)
    body += input_page % {'content': codefield % { 'codeblock': codeblock_content}}
    body += return_footer
    return body


def main():
    print "Content-type:text/html\r\n\r\n"
    cgitb.enable()
    settings = Settings('/etc/admin/settings.yaml')

    form = cgi.FieldStorage() 
    if form.getvalue('action'):
        action = form.getvalue('action')
    else: 
        errormessage(message='Page Not Found', reason='The page you requested could not be found, either contact your webmaster or try again.')

    present = False
    for command in settings.commands:
        if action == settings.commands[command]['id']:
            present = True
            run = command

    if not present:
        errormessage(message='Unknown action', reason='The action you requested has an existential crisis, either read the fucking manual or try again.')
    
    command_output = get_command_content(settings=settings, script=run)
    body = { 'body': command_output}
    print template % body


main()
