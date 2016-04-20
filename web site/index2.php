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

	<div class="container-fluid text-center"> 
		<?php
    // select a database and collection
		$m = new Mongo();
		$db = $m->selectDB('eventDB');
		$collection = new MongoCollection($db, 'events');
    // list all unique cities in DB
		$list_cities = $collection->distinct("city");
		$list_tags = $collection->distinct("tags");
		sort($list_tags);
		sort($list_cities);
    //$list_cities->sort(array("city"=>1));
		?>
		<div class="container fluid">
			<div class="row">
				<div class="col-sm-3 text-left">
					<div class="panel panel-default">
						<div class="panel-heading"><h4>Filter your search</h4></div>
						<div class="panel-body">
							<?php
							echo "<form>";
							echo '<div class="dropdown">';
							echo '<button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown" id="dropdownCity">City   <span class="caret"></span></button>';
							echo  '<ul class="dropdown-menu" aria-labelledby="dropdownCity">';
							for($index = 0; $index <= sizeof($list_cities) - 1; $index++){
								echo '<li><a href="#">';
								echo $list_cities[$index];
								echo '</a></li>';
							} 
							echo '</ul>';
							echo '</div>';
							echo '<br>';
							echo '<div class="dropdown">';
							echo '<button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown"><span>Keywords </span> <span class="caret"></span></button>';

							echo '<ul class="dropdown-menu">';
							for($index = 0; $index <= sizeof($list_tags) - 1; $index++){
								echo '<div class="checkboxdiv">'; 
								echo  '<label><input type="checkbox" value="" class="cBox" id=';
								echo $list_tags[$index];
								echo '> ';
								echo $list_tags[$index];
								echo '<label>';
								echo '</div>';
							}
							echo '</ul>';
							echo '</div>';
							echo '<br>';
							echo '<br>';
							echo '<br>';
							echo '<button class="btn btn-default position-right" type="reset" id="resetFilter">Reset Filters</button>';
							echo "</form>";?>
						</div>
					</div>
				</div>
				<div class="col-sm-8 text-left"> 
					<div class="panel-group">
						<?php
        // define variables and set to empty values
						$title = $host = $city = $date = $url = $time = "";
						$city = (isset($_POST['city']) ? $_POST['city'] : '');
						$today = date("Y-m-d");
						$cityQuery = array('city' => $city, 'date'=> array('$gte'=>$today));
						$afterToday=array('date'=> array('$gte'=>$today));

						$query = $collection->find($afterToday);
						$query->sort(array("date"=>1));
						foreach ( $query as $current ){
							echo '<div class="panel panel-primary">';
							echo '<a href="'.$current["url"].'"><div class="panel-heading"><h3 id="title-text">' . $current["title"];
							echo '</h3></div></a>';
							echo '<div class="panel-body">';
							echo '<strong>City: </strong>' . (!empty($current["city"]) ? $current['city'] : "");
							echo "<br>";
							echo '<strong>Host: </strong>' . (!empty($current["host"]) ? $current['host'] : "");
							echo "<br>";
							echo '<strong>Date: </strong>' . (!empty($current["date"]) ? $current['date'] : "");
							echo "<br>";
							echo '<strong>Time: </strong>' . (!empty($current["time"]) ? $current['time'] : "");
							echo "<br>";
							echo '<strong>Description: </strong>' . (!empty($current["description"]) ? $current['description'] : "");
							echo "<br>";
							echo '<strong>Tags: </strong>'; 
							$tags = $current["tags"];
							$len=count($tags);
							for ($i=0;$i<$len;$i++)
								echo $tags[$i] . " ";
							echo '</pre>';
							echo "<br>";
							echo '</div>';
							echo '</div>';
						}
						?>
					</div>
				</div>
			</div>
		</div>
		<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
		<!-- Include all compiled plugins (below), or include individual files as needed -->
		<script src="js/bootstrap.min.js"></script>
		<!-- Changes the viewed value in on the drop down menus when selected -->
		<script> $(".dropdown-menu li a").click(function(){
			$(this).parents(".dropdown").find('.btn').html($(this).text() + ' <span class="caret"></span>');
			$(this).parents(".dropdown").find('.btn').val($(this).data('value'));
			$(".panel-primary:not(:contains('"  + $(this).text() + "'))").hide();
			$(".panel-primary:contains('"  +'City: '+ $(this).text() + "')").show();
		});
	</script>
	<script>
		$(function() {
			$("#resetFilter").trigger("click");
		});
	</script>
	<script>
		$("#resetFilter").on("click", function(){
			$("#dropdownCity").button("reset")
			$('.cBox').change();
		});
	</script>
	<script>
		$('.cBox').change(function() {
			var checkID = $(this).attr("id");
			if( $(this).is(':checked')) {
				$(".panel-primary:not(:contains('" + checkID + "'))").hide();
        //$(".panel-primary").hide();
    } else {
    	$(".panel-primary:not(:contains('" + checkID + "'))").show();
    } 
}); 
</script>

</body>
</html>