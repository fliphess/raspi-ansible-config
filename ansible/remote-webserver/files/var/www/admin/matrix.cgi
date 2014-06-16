#!/usr/bin/python
import cgi
import cgitb 
from string import Template

from matrix.settings import Settings

from matrix.html.header import header
from matrix.html.modal import modal

print "Content-Type: html";


def starlinks(settings):
    body = """<div class="row">"""

    for command in sorted(settings.commands):
        if 'star' in settings.commands[command] and settings.commands[command]['star']:
            body += """
<div class="col-6 col-sm-6 col-lg-4">
  <h2>%s</h2>
  <p>%s</p>"""
	    body += modal % {'key': 'plop', 'name': 'gnoffel', 'content': 'srlkgmgaegergaergae'}
            body += """
</div><!--/span-->"""

    body += """</div><!--/row-->"""
    return body


def sidelinks(settings):
    body = """
<div class="col-xs-6 col-sm-3 sidebar-offcanvas" id="sidebar" role="navigation"> 
  <div class="list-group">
    <a class="list-group-item"><b>Links</b></a>"""
    for link in sorted(settings.links):
        body += """<a href="%s" class="list-group-item">%s</a>""" % ('link', 'title'.title())
    body += "</div>"
    return body


def page(settings):
    body = """<body>
<div class="container">
  <div class="row row-offcanvas row-offcanvas-right">

    <div class="col-xs-12 col-sm-9">
      <p class="pull-right visible-xs">
        <button type="button" class="btn btn-primary btn-xs" data-toggle="offcanvas">Toggle nav</button>
      </p>
    <div class="jumbotron">
  
    <h1>Startpage</h1>
    <p>Pages of all tools</p>
  </div>"""

    body += starlinks(settings)
    body += """</div><!--/span-->"""

    body += sidelinks(settings)
    body += """</div><!--/span-->"""

    body += """
        </div><!--/span-->
      </div><!--/row-->
    </div><!--/.container-->"""
    
    body += """
    <script src="/static/jquery.min.js"></script>
    <script src="/static/bootstrap.min.js"></script>
    <script src="/static/offcanvas.js"></script>
  </body>
</html>"""
    return body


cgitb.enable()
settings = Settings('/etc/admin/settings.yaml')

print header
print page(settings=settings)
