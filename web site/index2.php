<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
	<!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
	<title>ÅF Event Calendar</title>

	<!-- Bootstrap -->
	<link href="css/bootstrap.css" rel="stylesheet">
</head>
<body>
	<nav class="navbar navbar-default navbar-fixed-top text-center">
		<div class="container" style="float: center">
			<img src="af_logotype.png" style="float: left; width:68px;height:68px;">
			<h1 id="header-text" style="float: center">Event Calendar</h1>
		</div>
	</nav>

	<div class="container">
		<div class="row">
			<div class="col-sm-3">
				<div class="sidebar-nav">
					<div class="navbar navbar-default" role="navigation">
						<div class="navbar-header">
							<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".sidebar-navbar-collapse">
								<span class="sr-only">Toggle navigation</span>
								<span class="icon-bar"></span>
								<span class="icon-bar"></span>
								<span class="icon-bar"></span>
							</button>
							<span class="visible-xs navbar-brand">Sidebar menu</span>
						</div>
						<div class="navbar-collapse collapse sidebar-navbar-collapse">
							<ul class="nav navbar-nav">
								<li class="active"><a href="#">Menu Item 1</a></li>
								<li><a href="#">Menu Item 2</a></li>
								<li class="dropdown">
									<a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
									<ul class="dropdown-menu">
										<li><a href="#">Action</a></li>
										<li><a href="#">Another action</a></li>
										<li><a href="#">Something else here</a></li>
										<li class="divider"></li>
										<li class="dropdown-header">Nav header</li>
										<li><a href="#">Separated link</a></li>
										<li><a href="#">One more separated link</a></li>
									</ul>
								</li>
								<li><a href="#">Menu Item 4</a></li>
								<li><a href="#">Reviews <span class="badge">1,118</span></a></li>
							</ul>
						</div><!--/.nav-collapse -->
					</div>
				</div>
			</div>
			<div class="col-sm-6">
				<div class="panel-group">
					<div class="panel panel-default">
						<div class="panel-heading">Panel Header</div>
						<div class="panel-body">Panel Content</div>
					</div>
					<div class="panel panel-default">
						<div class="panel-heading">Panel Header</div>
						<div class="panel-body">Panel Content</div>
					</div>
					<div class="panel panel-default">
						<div class="panel-heading">Panel Header</div>
						<div class="panel-body">Panel Content</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</body>
</html>