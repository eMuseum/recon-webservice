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
        <h1>Recognition result</h1>
		<p>Your image has been recognized as: <b>{{ name }}</b> </p>
		<p><img src="{{ get_url('images', filename=img) }}" class="img-recon" /></p>
		<p><a class="btn-start btn-lg btn-success" href="/" role="button">Back</a></p>
	  </div>

      <div class="footer">
        <p>&copy; eMusum 2014</p>
      </div>

    </div> <!-- /container -->
