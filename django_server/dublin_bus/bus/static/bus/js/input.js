src="{% static 'bus/js/map_init.js' %}"

// Author: Stacy 

// This JQuery Function creates the date and time picker as well as limits the dates selectable by having the minimum date always be today.


$(document).ready(function () {
  var today = new Date();
  var end = moment(today).add(6, 'M');
    $('#datetimepicker4').datetimepicker({
        minDate: today,
        maxDate: end,
        format: 'DD/MM/YY LT',
        date: moment(),
        icons:{
          time:'far fa-clock',
          date: 'fa fa-calendar',
	      	up: 'fa fa-angle-up',
		      down: 'fa fa-angle-down',
		      previous: 'fa fa-angle-left',
		      next: 'fa fa-angle-right',
		      today: 'fa fa-dot-circle-o',
		      clear: 'fa fa-trash',
		      close: 'fa fa-times'
          }
});
});
// This Jquery function should change the text on the show/hide menu button when pressed 

  $("#JP-btn").click(function(e){
    e.preventDefault(); //prevents the need to double click
    $('#floating-panel').toggle();
    if($('#floating-panel').is(':visible')) {
        $(this).html('Hide Planner');
    } else {
        $(this).html('Show Planner');
    }
});
$("#BS-btn").click(function(e){
  e.preventDefault(); //prevents the need to double click
  $('#searchStopNumber').toggle();
  if($('#searchStopNumber').is(':visible')) {
      $(this).html('Hide Search');
  } else {
      $(this).html('Show Search');
  }
});
// This function takes the values entered into the intputs on the index page and re prints them out. 
function myFunction() {
  var input1 = document.getElementById("searchTextField_start").value;
  var input2 = document.getElementById("searchTextField_destination").value;
  for (i=0; i < stepList.length; i++) {
    text += "<li>" + stepList[i] + " " + "(Duration: " + durationList[i] + ")" + "</li>";
    // console.log(text);
    document.getElementById("test").innerHTML = text;
    // document.getElementById("test").innerHTML = "Step " + route.steps.length + ":" + stepList;
    document.getElementById("test1").innerHTML = " Start: " + input1; 
    document.getElementById("test2").innerHTML = " Destination: " + input2;
    // document.getElementById("test3").innerHTML = "Estimated arrival Time: " + arr;
  }
  text =+ "</ol>";
}
  function myFunction2() {
    var input1 = document.getElementById("searchStopNumber").value;
    document.getElementById("stop").innerHTML = "Stop " + input1 + ": Bus, Destination, and Predicted time of arrival"; 
  }
  // Below is the code for the direction planner
  //first we show the planner
    $('#submit-btn').click(function(){
      $('#directions').show({
        bottom: '-300px',
        height:'400px',
        position: 'absolute',
      });
    });
    //then we can close the planner
   $("#close").click(function(){
      $("#directions").hide();
    });
    //then we can animate the planner each time!
    $('#submit-btn').click(function() {
      $('#directions').animate({
        bottom: '-300px',
        height: '400px',
        position: 'absolute',
      });
    });



var initMap = function() {
  var userLocation = {
    lat: 53.33498053,
    lng: -62603097
  };
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 16,
    center: userLocation
  });
  var marker = new google.maps.Marker({
    position: userLocation,
    map: map
  });
  markers.push(marker);
}(position) {
  var userLatLng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
  var marker = new google.maps.Marker({
    position: userLatLng,
    title: 'Your Location',
    draggable: true,
    map: map
  });
  markers.push(marker);
  var bounds = new google.maps.LatLngBounds();
  for (var i = 0; i < markers.length; i++){
    bounds.extend(markers[i].getPosition());
  }
  map.firBounds(bounds);
}
function errorHandler(error) {
  console.log('Geolocation error : code ' + error.code + ' -- ' + error.message);
}
initMap(); 

navigator.geolocation.getCurrentPosition(showPosition, errorHandler, {
  enableHighAccuracy: false,
  maximumAge: 60000,
  timeout: 27000
});
var geo = document.getElementById("ok");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    geo.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  geo.innerHTML = "Latitude: " + position.coords.latitude +
  "<br>Longitude: " + position.coords.longitude;
}
// function showPosition(position) {
//   var latlon = position.coords.latitude + "," + position.coords.longitude;

//   var img_url = "https://maps.googleapis.com/maps/api/staticmap?center=" + latlon + "&zoom=14&size=400x300&sensor=false&key=AIzaSyCFtH8qWuX2LGmHcicY-vLHfYuB7D6WI7Y&libraries=places&callback=initMap";

//   document.getElementById("").innerHTML = "<img src='"+img_url+"'>";
// }