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
      <div class="container" style="float: center">
        <img src="af_logotype.png" style="float: left; width:68px;height:68px;">
        <h1 id="header-text" style="float: center">Event Calendar</h1>
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
        $list_tags = $collection->distinct("tags");
        //$list_cities->sort(array("city"=>1));

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
        <div class="col-md-2 text-left">
          <div class="panel panel-default">
          <div class="panel-heading">Filter your search</div>
            <div class="panel-body">
          <?php
            echo "<form>";
            // echo '<div class="dropdown">';
            // echo '<button class="btn btn-primary dropdown-toggle" type="button" id="dropdownCity" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">';
            // echo 'City  ';
            // echo    '<span class="caret"></span>';
            // echo  '</button>';
            // echo  '<ul class="dropdown-menu" aria-labelledby="dropdownCity">';
            // for($index = 0; $index <= sizeof($list_cities) - 1; $index++){
            //   echo '<li><a href="#">';
            //   echo $list_cities[$index];
            //   echo '</a></li>';
            // } 
            // echo '</ul>';
            // echo '</div>';
            echo '<br>';
            echo '<div class="dropdown">';
            echo '<button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown" id="dropdownCity">City   <span class="caret"></span></button>';
            echo  '<ul class="dropdown-menu" aria-labelledby="dropdownCit">';
            for($index = 0; $index <= sizeof($list_cities) - 1; $index++){
              echo '<li><a href="#">';
              echo $list_cities[$index];
              echo '</a></li>';
            } 
            echo '</ul>';
            echo '</div>';
            // echo '<div class="dropdown">';
            // echo '<button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">';
            // echo    'Type    ';
            // echo    '<span class="caret"></span>';
            // echo  '</button>';
            // echo  '<ul class="dropdown-menu" aria-labelledby="dropdownMenu1">';
            // echo    '<li><a href="#">Action</a></li>';
            // echo    '<li><a href="#">Another action</a></li>';
            // echo    '<li><a href="#">Something else here</a></li>';
            // echo '</ul>';
            // echo '</div>';
            echo '<br>';
            
            for($index = 0; $index <= sizeof($list_tags) - 1; $index++){
            echo '<div class="checkbox">'; 
            echo  '<label><input type="checkbox" value="">';
            echo    $list_tags[$index];
            echo  '<label>';
            echo '</div>';
            }
            echo '<br>';
            echo '<br>';
            echo '<br>';
            echo '<button type="button" class="btn btn-success" id="filter">Filter</button>';
            echo '<button class="btn btn-default position-right" type="reset" id="resetFilter">Reset Filters</button>';
            echo "</form>";

            ?>
            </div>
          </div>
         </div>

        <div class="col-sm-8 text-left"> 
          <div class="container-fluid">
            <div class="panel-group">
              <?php
                // define variables and set to empty values
                $title = $host = $city = $date = $url = $time = "";
                $city = (isset($_POST['city']) ? $_POST['city'] : '');
                $today = date("Y-m-d");
                $cityQuery = array('city' => $city, 'date'=> array('$gte'=>$today));
                $afterToday=array('date'=> array('$gte'=>$today));
                //if "Select city" is chosen in drop down menu, select all cities
                if ($_POST['city'] == 'cities') {
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
                // select the city corresponding to the drop down menu
                } else {
                  $query = $collection->find($cityQuery);
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
    <!-- Changes the viewed value in on the drop down menus when selected -->
    <script> $(".dropdown-menu li a").click(function(){
      $(this).parents(".dropdown").find('.btn').html($(this).text() + ' <span class="caret"></span>');
      $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
      });
    </script>
    <script>
    jQuery(function(){
      jQuery('#resetFilter').click();
    });
    </script>
    <script>
        $("#resetFilter").on("click", function(){
         $("#dropdownCity").button("reset")
        });
    </script>
  </body>
</html>