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

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <nav class="navbar navbar-default navbar-fixed-top text-center">
      <div class="container">
        <h1 id="header-text">ÅF Event Calendar</h1>
      </div>
    </nav>
    
    <div class="container-fluid text-center"> 

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

       <div class="row content">
        <div class="col-sm-2 sidenav text-left">
          <div class="dropdown">
            <button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
              City
              <span class="caret"></span>
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">
            <?php> 
            for($index = 0; $index <= sizeof($list_cities); $index++){
              echo '<li><a href="#">Action</a></li>';
            }
            <?>
            </ul>
          </div>
          <br>
          <div class="dropdown">
            <button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
              Type
              <span class="caret"></span>
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">
              <li><a href="#">Action</a></li>
              <li><a href="#">Another action</a></li>
              <li><a href="#">Something else here</a></li>
            </ul>
          </div>

         </div>

        <div class="col-sm-8 text-left"> 
          <div class="container-fluid">
            <div class="panel-group">
      <?php
        // define variables and set to empty values
        $title = $host = $city = $date = $url = $time = "";
          $city = (isset($_POST['city']) ? $_POST['city'] : '');
        $cityQuery = array('city' => $city);
        //if "Select city" is chosen in drop down menu, select all cities
        if ($_POST['city'] == 'cities') {
          $query = $collection->find();
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
            echo '</div>';
            echo '</div>';
               
        }
        // select the city corresponding to the drop down menu
        } else {
          $query = $collection->find($cityQuery);
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
            echo '</div>';
            echo '</div>';
          }
        }
      ?>

        </div>
      </div>
    </div>




    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>