<!DOCTYPE html>
<html>
	<head>
		<link rel="stylesheet" type="text/css" href="mystyle1.css">
		<title>ÅF Event Calendar</title>
		<meta charset="UTF-8">
	</head>

	<body>
		<div id="header">
			<h1>ÅF Event Calendar</h1>
		</div>

		<div id="filter">
			<h2> Filter search</h2>
			<?php
			   // connect to mongodb
			   //$m = new MongoClient();
			   
			   // select a database and collection
				$m = new Mongo();
				$db = $m->selectDB('eventDB');
				$collection = new MongoCollection($db, 'events');
				// list all unique cities in DB
				$list_cities = $collection->distinct("city");

				echo '<form method=POST>';
			  	echo '<select name="city">';
			  	echo '<option value="cities">Select city</option>';
			  	for($index = 0; $index <= sizeof($list_cities); $index++){
					echo "<option value=$list_cities[$index]>$list_cities[$index]</option>";
			  	}
			    
			  	echo  '</select>';
			  	echo '<br>';
			  	echo '<input name="filter_search" type="submit">';
				echo '</form>';
			?>
		</div>

		<div id = "section">
			<?php
				// define variables and set to empty values
				$title = $host = $city = $date = $url = $time = "";
			    $city = (isset($_POST['city']) ? $_POST['city'] : '');
				$cityQuery = array('city' => $city);
				//if "Select city" is chosen in drop down menu, select all cities
				if ($_POST['city'] == 'cities') {
					$query = $collection->find();
					foreach ( $query as $current ){
						echo '<div class="event">';
						echo '<a href="'.$current["url"].'" target="_blank"><h3>' . $current['title'];
						echo '</h3></a>';
						echo "<br>";
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
						//echo' <a href="'.$current["url"].'" target="_blank"> '." --> To the event" .'</a>';
						echo '</div>';
						echo "<br>";
					}
				// select the city corresponding to the drop down menu
				} else {
					$query = $collection->find($cityQuery);
					foreach ( $query as $current ){
						echo '<div class="event">';
						echo '<a href="'.$current["url"].'" target="_blank"><h3>' . $current['title'];
						echo '</h3></a>';
						echo "<br>";
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
						//echo' <a href="'.$current["url"].'" target="_blank"> '." --> To the event" .'</a>';
						// echo 'More information:'.' <a href="'.$current["url"].'" target="_blank"> '.$current["url"] .'</a>';
						echo '</div>';
						echo "<br>";
					}
				}
			?>
		</div>
	</body>
</html>