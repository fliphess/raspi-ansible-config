from matrix.html.error import error
from matrix.html.template import template, codefield
from matrix.html.template import alert_ok, alert_nok
from matrix.html.template import input_page, return_footer
import cgi
import sys
import subprocess

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


def get_command_content(settings, script, page='control'):
    body = ''
    if page == 'system':
        element = settings.system[script]
    else:
        element = settings.commands[script]

    output, exitcode = run_command(element['command'])
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
    body += return_footer % {'id': element['id']}
    return body

