<title>Work Orbit</title>
<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
<link rel="stylesheet" type="text/css" href="/style.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<script src="/script.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCLhw12hTzbrWIAIepH3EoDvKGs1WhetTQ"></script>
<script type="text/javascript" src="https://apicdn.walkscore.com/api/v1/traveltime_widget/js?wsid=3950dacfe4b9f83564d394cab5e9fb88"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<script src="//cdn.jsdelivr.net/rsvp/3.0.6/rsvp.js"></script>

<script type="text/javascript">
'use strict';
// What is the data structure of a polygon? //
var clickablePolygons = [];
var infoWindow = new google.maps.InfoWindow({ size: new google.maps.Size(100,50) });

// This function is called after the HTML is finished loading.
// It is passed in as a callback to:
// google.maps.event.addDomListener(window, 'load', initialize);
function initialize() {

  var address = document.URL.split('/')[6];
  address = address.replace(/%20/g,' ');

  var mapCanvas  = document.getElementById('map-canvas');
  var mapOptions = {
    mapTypeId : google.maps.MapTypeId.ROADMAP,
    center    : new google.maps.LatLng(47.6222788,-122.336828599),
    zoom      : 13
  };

  // This creates the actual map object and attaches it to the HTML object //
  var map = new google.maps.Map( mapCanvas, mapOptions );

  var promiseGeocode = new RSVP.Promise(function (resolve, reject) {
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode( { 'address': address}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        var location = results[0].geometry.location
        var lat = location.k;
        var lng = location.D;
        location = lat + ',' + lng;
        resolve(location);

      } else {
        alert("Geocode was not successful for the following reason: " + status);
        reject("REJECTION");
      }
    });
  });

  promiseGeocode.then( function(location) {
    // Loads the big JSON //
    map.data.loadGeoJson('https://s3.amazonaws.com/work-orbit/all_Seattle_data_test.geojson', {idPropertyName:"name"});

    var time = Number.parseInt(document.URL.split('/')[4]);
    var mode = document.URL.split('/')[5];

    // Data Imports //
    var neighborhoods = map.data.loadGeoJson('https://s3.amazonaws.com/geohackers-for-good/seattle_named_neighborhoods.geojson');

    if (mode == "bike") {
      var pronto = map.data.loadGeoJson('https://s3.amazonaws.com/geohackers-for-good/pronto_locations.geojson');
    }

    // Styling the Data //
    var mode_map = {
      'car': walkscore.TravelTime.Mode.DRIVE,
      'walk': walkscore.TravelTime.Mode.WALK,
      'bike': walkscore.TravelTime.Mode.BIKE,
      'bus': walkscore.TravelTime.Mode.TRANSIT
    };

    var widget = new walkscore.TravelTimeWidget({
      map: map,
      origin: location,
      show: true,
      mode: mode_map[mode],
      time: time,
      congestion: true
    });
  });

  // Add the click listener for events //
  map.data.addListener('click', function(event) {
    // Populate the string //
    var promiseModal = new RSVP.Promise(function (resolve, reject) {

      var data_str  = '<div> Welcome to ' + event.feature['k']['name'] + '. ';
      data_str += 'The median household income is ' + event.feature['k']['Median_Household_Income'] + '. ';
      data_str += 'The average commute takes ' + event.feature['k']['Median_Commute_Time'] + ' minutes. ';
      data_str += 'The following jobs are common here: ';
      data_str += '<ul>';

      event.feature['k']['Employment'].forEach( function(job) {
          data_str += '<li>' + job + '</li>';
      });
      data_str += '</ul><br><div>';
      resolve(data_str);
    });

    promiseModal.then( function(data_str) {
    // Set walkscore widget center point
      infoWindow.setContent(data_str);

      var anchor = new google.maps.MVCObject();
      anchor.set("position",event.latLng);
      infoWindow.open(map,anchor);
    });
  });
} // The initialize function ends here //

// This calls the initialize() function (above) after the page loads //
google.maps.event.addDomListener(window, 'load', initialize);
</script>
