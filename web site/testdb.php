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
	echo 'City: ' . $current['city'] ."\n";
	echo 'Host: ' . $current['host'] ."\n";
	echo 'Date: ' . $current["date"] ."\n";
	echo 'Time: ' . $current["time"] ."\n";
	
	echo' <a href="'.$current["url"].'" target="_blank"> '." --> To the event" .'</a>';
	// echo 'More information:'.' <a href="'.$current["url"].'" target="_blank"> '.$current["url"] .'</a>';
	
	echo '</div>';
	echo "\n";
}
echo '</pre>';
?>
</text>
</body>
</html>