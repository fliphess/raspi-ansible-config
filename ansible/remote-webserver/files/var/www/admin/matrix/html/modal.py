from string import Template

modal = """
<div class="btn-group">
  <button class="btn btn-small btn-default" data-toggle="modal" data-target="#%(key)sModal">%(name)</button>
  <div class="modal fade" id="%(key)sModal" tabindex="-1" role="dialog" aria-labelledby="%(key)sModalLabel" aria-hidden="true" data-color="FF00000">
    <div class="modal-dialog">
      <div class="modal-content">

        <div class="modal-header">
          <h2 class="modal-title" id="%(key)sModalLabel">%(fullname)s</h2>
        </div>

        <div class="modal-header panel-default">
          <div class="modal-header panel-heading">
            <h4 class="modal-title" id="%(key)sModalLabel">Status:</h4>
            <h3 class="modal-title" id="%(key)sModalLabel">%(name)s</h3>
          </div>
        </div>

        <div class="modal-body">
	  %(content)s
        </div>

        <div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>
</div>
"""
