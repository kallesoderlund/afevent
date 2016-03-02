<!DOCTYPE html>
<html>
<head>
<title>ÅF Event Calendar</title>
<meta charset="UTF-8">
</head>
<body>

<h1>ÅF Event Calendar</h1>
<p>This is our data.</p>
<?php
   // connect to mongodb
   $m = new MongoClient();
   echo "Connection to database successfully";
   // select a database
   $db = $m->selectDB("eventDB");
   $collections = $db->listCollections();
   echo "Database $db selected";


?>
<?php
$db = new Mongo();
$query = $db->eventDB->events->find();

echo '<pre><h2>';

foreach ( $query as $current )
    print_r($current);

echo '</h2></pre>';
?>
</body>
</html>
