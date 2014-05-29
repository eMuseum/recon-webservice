<div class="container">
      <div class="header">
        <ul class="nav nav-pills pull-right">
          <li class="active"><a href="#">Home</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
        <h3 class="text-muted">eMuseum Recognition</h3>
      </div>

      <div class="jumbotron">
        <h1>Upload an image</h1>
		<form action="/upload" method="post" enctype="multipart/form-data">
			<p class="lead">Select a file: <input type="file" name="upload" /></p>
			<p><a class="btn btn-lg btn-success" href="javascript:void(0);" onclick="$(this).closest('form').submit();" role="button">Start Upload</a></p>
		</form>
      </div>

      <div class="row marketing">
        <div class="col-lg-6">
          <h4>Caffe</h4>
          <p>eMuseum recognition features Caffe neural net, from Berkeley.</p>

          <h4>Python</h4>
          <p>Everything is supported by Python, including this webservice.</p>

          <h4>Universitat de Barcelona</h4>
          <p>This project is hosted on Universitat of Barcelona.</p>
        </div>

        <div class="col-lg-6">
          <h4>Github</h4>
          <p>We are open source, all code can be found at <a href="https://github.com/eMuseum">Github</a>.</p>

          <h4>Android</h4>
          <p>eMuseum is an Android application which features QR reading and image recognition.</p>

          <h4>Acknowledgements</h4>
          <p>We are particularly grateful for the assistance given by Santi Seguí Mesquida.<br />We wish to acknowledge the help provided by Frances Dantí Espinasa.</p>
        </div>
      </div>

      <div class="footer">
        <p>&copy; eMusum 2014</p>
      </div>

    </div> <!-- /container -->
	