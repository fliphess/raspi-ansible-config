modal = """
<div class="col-6 col-sm-6 col-lg-4">
  <h2>%(title)s</h2>
  <p>%(name)s</p>

  <button class="btn btn-small btn-danger" data-toggle="modal" data-target="#%(tag)sModal">Run %(name)s</button>
  <div class="modal fade" id="%(tag)sModal" tabindex="-1" role="dialog" aria-labelledby="%(tag)sModalLabel" aria-hidden="true" data-color="FF00000">
    <div class="modal-dialog">
      <div class="modal-content">

        <div class="modal-header">
          <h2 class="modal-title" id="%(tag)sModalLabel">%(title)s</h2>
        </div>

        <div class="modal-header panel-heading">
          <div class="modal-title" id="%(tag)sModalLabel">Are you sure you want to continue?</div><br>
          <div class="modal-title" id="%(tag)sModalLabel">Click Yes to continue</div>
        </div>

        <div class="modal-footer">
          <form method="post" action="%(postscript)s">
          <input type="hidden" name="action" value="%(identifier)s" />
          <button type="submit" class="btn btn-default">Continue</button>
        </form>
      </div>
    </div>
  </div>
</div>
</div><!--/span-->
"""
