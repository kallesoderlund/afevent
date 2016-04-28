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
    $events = new MongoCollection($db, 'events');
    // list all unique locations in DB
    $list_locations = $events->distinct("location");
    $list_tags = $events->distinct("tags");
    $list_types = $events->distinct("type");
    sort($list_tags);
    sort($list_locations);
    sort($list_types);
    ?>

    <div class="container fluid">
      <div class="row">
        <div class="fixed col-sm-3 text-left">
          <div class="panel panel-default">
            <div class="panel-heading"><h4>Filter your search</h4></div>
            <div class="panel-body">
              <div class="row">

                <!--Dropdown for city of the events-->
                <div class="col-sm-8">
                  <div class="dropdown">
                    <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown"><span>Location </span> <span class="caret"></span></button>
                    <ul class="dropdown-menu scrollable-menu">
                      <?php
                      for($index = 0; $index <= sizeof($list_locations) - 1; $index++){
                        $location_count = ($events->count(array('location'=>$list_locations[$index])));
                        echo '<div class="checkboxdiv">'; 
                        echo  '<label><input type="checkbox" value="" class="cBox" id="Location: ';
                        echo $list_locations[$index];
                        echo '"> ';
                        echo $list_locations[$index] . ' (' . $location_count . ')';
                        echo '</label>';
                        echo '</div>';
                      }
                    ?>
                  </ul>
                </div>
              </div>

              <!-- Dropdown menu for tag of the events -->
              <div class="col-sm-8">
                <div class="dropdown">
                  <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown"><span>Type </span> <span class="caret"></span></button>
                  <ul class="dropdown-menu scrollable-menu">
                    <?php
                    for($index = 0; $index <= sizeof($list_types) - 1; $index++){
                      $type_count = ($events->count(array('type'=>$list_types[$index])));
                      echo '<div class="checkboxdiv">'; 
                      echo  '<label><input type="checkbox" value="" class="cBox" id=';
                      echo $list_types[$index];
                      echo '> ';
                      echo $list_types[$index] . ' (' . $type_count . ')';
                      echo '</label>';
                      echo '</div>';
                    }
                  ?>
                </ul>
              </div>
            </div>

            <!-- Dropdown menu for type of event -->
            <div class="col-sm-8">
              <div class="dropdown">
                <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown"><span>Keywords </span> <span class="caret"></span></button>
                <ul class="dropdown-menu scrollable-menu">
                  <?php
                  for($index = 0; $index <= sizeof($list_tags) - 1; $index++){
                  $tags_count = ($events->count(array('tags'=>$list_tags[$index])));
                  echo '<div class="checkboxdiv">'; 
                  echo  '<label><input type="checkbox" value="" class="cBox" id=';
                  echo $list_tags[$index];
                  echo '> ';
                  echo $list_tags[$index] . ' (' . $tags_count . ')';
                  echo '</label>';
                  echo '</div>';
                }
                ?>
              </ul>
            </div>
          </div>
        </div>
        <br>
        <br>
        <button class="btn btn-default position-right" type="reset" id="resetFilter">Reset Filters</button>
      </div>
    </div>
  </div>

  <div class="col-sm-8 text-left"> 
    <div class="panel-group">
      <?php
      // define variables and set to empty values
      $title = $host = $location = $date = $url = $time = "";
      $location = (isset($_POST['location']) ? $_POST['location'] : '');
      $today = date("Y-m-d");
      $locationQuery = array('location' => $location, 'date'=> array('$gte'=>$today));
      $afterToday=array('date'=> array('$gte'=>$today));
      $query = $events->find($afterToday);
      $query->sort(array("date"=>1));
      // For each event, create a panel
      foreach ( $query as $current ){
      echo '<div class="panel panel-primary">';
      echo '<a href="'.$current["url"].'"><div class="panel-heading"><h3 id="title-text">' . $current["title"];
      echo '</h3></div></a>';
      echo '<div class="panel-body">';
      echo '<strong>Location: </strong>' . (!empty($current["location"]) ? $current['location'] : "");
      echo "<br>";
      echo '<strong>Date: </strong>' . (!empty($current["date"]) ? $current['date'] : "");
      echo "<br>";
      echo '<strong>Type: </strong>' ; 
      $type = $current["type"];
      sort($type);
      $len=count($type);
      for ($i=0;$i<$len;$i++)
      echo $type[$i] . " ";
      echo "<br>";
      echo "<br>";
      echo  (!empty($current["description"]) ? $current['description'] : "");
      echo "<br>";
      echo '<hr class="divider">';
      echo '<font size="2" color="#999999">'; 
      $tags = $current["tags"];
      sort($tags);
      $len=count($tags);
      for ($i=0;$i<$len;$i++)
      echo '<u>' . $tags[$i] . '</u>, ';
      echo "</font><br>";
      echo '</pre>';
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
<script>
  $(function() {
    $("#resetFilter").trigger("click");
  });
</script>
<!-- Resets all filters when pressing the Reset filters button -->
<script>
  $("#resetFilter").on("click", function(){
    $("#dropdownLocation").button("reset")
            $('.cBox').prop('checked', false); // Unchecks it
            countCheckedCheckboxes = 0;
            $('.panel-primary').show();
          });
        </script>
        <!--Counts how many checkboxes are checked. If 0, then show all. When checked, loop through them and show the events that matches the checked, hide the rest. -->
        <script>
          $(document).ready(function(){
            var $checkboxes = $('[type="checkbox"]');
            $('.cBox').change(function() {
              var countCheckedCheckboxes = $checkboxes.filter(':checked').length;
              $('input[type=checkbox]').each(function () {
                var thisID = $(this).attr("id");
                $(".panel-primary:not(:contains('" + thisID + "'))").hide();
              });
              $('input[type=checkbox]').each(function () {
                var thisID = $(this).attr("id");
                if( $(this).is(':checked')) {
                  console.log(thisID)
                  $(".panel-primary:contains('" +thisID+ "')").show();
                };
                if (countCheckedCheckboxes == 0){
                  $('.panel-primary').show();
                }
              });
            });
          });
        </script>
      </body>
      </html>