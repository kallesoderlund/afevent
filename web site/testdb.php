<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
<title>ÅF Event Calendar</title>
<meta charset="UTF-8">
</head>
<body>

<AFtitel>ÅF Event Calendar</AFtitel>
<text>
<?php
   // connect to mongodb
   $m = new MongoClient();
   
   // select a database
   $db = $m->selectDB("eventDB");
   $collections = $db->listCollections();

$db = new Mongo();
$query = $db->eventDB->events->find();

echo '<pre>';
foreach ( $query as $current ){
	echo '<div>';
	echo '<title_text>' . $current['title'];
	echo '</title_text>';
	echo "\n";
	echo 'City: ' . (!empty($current['city']) ? $current['city'] : "")."\n";

	echo 'Host: ' . (!empty($current['host']) ? $current['host'] : "")."\n";
	echo 'Date: ' . (!empty($current['date']) ? $current['date'] : "")."\n";
	echo 'Time: ' . (!empty($current['time']) ? $current['time'] : "")."\n";
	echo 'Description: ' . (!empty($current['description']) ? $current['description'] : ""). "\n";
	echo 'Long Description: ' . (!empty($current['long_description']) ? $current['long_description'] : ""). "\n";
	
	
	echo' <a href="'.$current["url"].'" target="_blank"> '." --> To the event" .'</a>';
	
	echo '</div>';
	echo "\n";
}



echo '</pre>';
?>
</text>
</body>
</html>
