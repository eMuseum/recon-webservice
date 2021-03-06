<html lang="en">
	<header>
		<title>eMuseum Recognition</title>
		
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		
		<link href="{{ get_url('static', path='css/bootstrap.min.css') }}" rel="stylesheet">
		<link href="{{ get_url('static', path='css/jumbotron-narrow.css') }}" rel="stylesheet">
		
		<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
		<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
		<!--[if lt IE 9]>
			<script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
			<script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
		<![endif]-->
	</header>
	<body>
	
	<div class="container">
      <div class="header">
        <ul class="nav nav-pills pull-right">
          <li {{ "class=active" if route == '/' else "" }}><a href="/">Home</a></li>
          <li {{ "class=active" if route == '/about' else "" }}><a href="/about">About</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
        <h3 class="text-muted">eMuseum Recognition</h3>
      </div>