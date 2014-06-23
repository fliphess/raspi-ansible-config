template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Control Matrix</title>
  <link href="/static/bootstrap.min.css" rel="stylesheet">
  <link href="/static/offcanvas.css" rel="stylesheet">
</head>

<body>

    %(body)s

    <script src="/static/jquery.min.js"></script>
    <script src="/static/bootstrap.min.js"></script>
    <script src="/static/offcanvas.js"></script>
  </body>
</html>

"""

codefield = """
<div class="highlight"><pre><code class="html">
%(codeblock)s
</code></pre></div>
</div>"""

alert_ok = """<div class="alert alert-success">OK! Command %(command)s executed successfully with exitcode %(exitcode)s</div>"""
alert_nok = """<div class="alert alert-danger">Error! Command %(command)s executed with non-zero exitcode %(exitcode)s</div>"""

input_page = """
<div class="container">
  <div class="row">
    %(content)s
  </div>
</div>"""

return_footer = """
<div class="container">
  <div class="row">
    <div class="alert alert-info">
      <a href="/admin/matrix.cgi" class="btn btn-large btn-info"><i class="icon-home icon-white"></i>Home</a>
    </div>
  </div>
</div>"""
