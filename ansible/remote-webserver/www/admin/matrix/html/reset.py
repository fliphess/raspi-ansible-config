indexpage = """
<div class="container">
  <div class="row row-offcanvas row-offcanvas-right">

    <div class="col-xs-12 col-sm-9">
      <p class="pull-right visible-xs"><button type="button" class="btn btn-primary btn-xs" data-toggle="offcanvas">Toggle nav</button></p>

      <div class="jumbotron">
        <h1>Pi Reset</h1>
        <p>Reset or turn off the raspberry pi</p>
      </div>

      <div class="row">
          %(mainfield)s
      </div>
    </div>

    <div class="col-xs-6 col-sm-3 sidebar-offcanvas" id="sidebar" role="navigation"> 
      <div class="list-group">
        <a class="list-group-item"><b>Links</b></a>

            %(sidefield)s
        </div>
      </div><!--/span-->
    </div><!--/span-->

  </div><!--/row-->
</div><!--/.container-->
"""
