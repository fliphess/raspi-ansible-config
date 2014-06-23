error = """ 
<div class="container">
  <div class="row">
    <div class="span12">
      <div class="hero-unit center">
          
	  <center>
	    <h1>%(message)s   <small><font face="Tahoma" color="red">Error 404</font></small></h1>
	    <p>An error appeared! The given reason was: %(reason)s
	      Use your browsers <b>Back</b> button to navigate to the page you previously came from</p>
            <p><b>Or you could just press this neat little button:</b></p>
            <a href="/admin/matrix.cgi" class="btn btn-large btn-info"><i class="icon-home icon-white"></i> Take Me Home</a>
            <br />
            <p></p>
          </center>

       </div>
    </div>
  </div>
</div>

"""
