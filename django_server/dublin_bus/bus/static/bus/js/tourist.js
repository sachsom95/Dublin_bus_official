//Author: Stacy
//This file powers the tourism panel, by giving the geolocation of the user and then routing them to a desired, 
// preselected, tourist destination! There are three parts to the logic, 1. Getting the current position of the user.
// 2. diplaying the current location on the map. and 3. calculating the route between the current location and the destination .  


// The section below initiates the direction service and some variables
directionsService = new google.maps.DirectionsService();
directionsDisplay = new google.maps.DirectionsRenderer();
let start_marker;
let end_marker ;
let destination;
let marker;

//this places a marker on the map when a user clicks on a certain location
function placeMarker(location) {
    marker = new google.maps.Marker({
        position: location, 
        map: map,
    });
}

//This listens for when a user clicks on the map and then it passes the event to the place marker function 
google.maps.event.addListener(map, 'click', function(event) {
    directionsDisplay.setMap(map);
    placeMarker(event.latLng);
    navigator.geolocation.getCurrentPosition(function(position){
    var here = new google.maps.LatLng(position.coords.latitude, position.coords.longitude); 
    destination = event.latLng;
    calcRoute(here, destination);
});

});
    
// this function uses geolocation to find an approximate location of the user.
function getLocation(){
    navigator.geolocation.getCurrentPosition(function(position){
        var pos = new google.maps.LatLng(position.coords.latitude, position.coords.longitude); // this is the user's location! 
        initMap(pos); // the location is then passed to the initMap function to be found on the map! 
    });
}

//Below is the function for putting the user's location on our map. 
function initMap(location){ 
    map = new google.maps.Map(document.querySelector("#map"),{
        center: location,
        zoom: 16,
    });
    directionsDisplay.setMap(map);
    calcRoute(location, destination); // this call the calcRoute function and passes the current location and desired destination to the function
}

// These are hard coded suggestions of popular tourist destinations.
// The user can click these to get started or click directly on the map for a more personalized search.
// Code altered from the google maps API
function Search_tourist(){
    const geocoder = new google.maps.Geocoder();
    geocodeAddress(geocoder, map);
    function geocodeAddress(geocoder, resultsMap) {
    const address = document.getElementById("address").value;
    geocoder.geocode({ address: address }, (results, status) => {
      if (status === "OK") {
        resultsMap.setCenter(results[0].geometry.location);
        new google.maps.Marker({
          map: resultsMap,
          position: results[0].geometry.location
        });
      } else {
        alert("Geocode was not successful for the following reason: " + status);
      }
   
    // var there = results[0].geometry.location;
    // console.log("hello hello hello" + resultsMap);
    there = results[0].geometry.location;
    // console.log(geocoder);
    navigator.geolocation.getCurrentPosition(function(position){
        var here = new google.maps.LatLng(position.coords.latitude, position.coords.longitude); 
        directionsDisplay.setMap(map); 
        // console.log(there);
        calcRoute(here, there);
    })
    });
};
}

function Guinness(){
    GST = new google.maps.LatLng(53.341978,-6.2889051);
    navigator.geolocation.getCurrentPosition(function(position){
        var here = new google.maps.LatLng(position.coords.latitude, position.coords.longitude); 
        calcRoute(here, GST);
        directionsDisplay.setMap(map);
        
});
}
function Trinity(){
    Trin = new google.maps.LatLng(53.3437935,-6.2567656);
    navigator.geolocation.getCurrentPosition(function(position){
        var here = new google.maps.LatLng(position.coords.latitude, position.coords.longitude); 
        calcRoute(here, Trin);
        directionsDisplay.setMap(map);
        
});
}
function Grafton(){
    Graf = new google.maps.LatLng(53.3422917,-6.2619447);
    navigator.geolocation.getCurrentPosition(function(position){
        var here = new google.maps.LatLng(position.coords.latitude, position.coords.longitude); 
        directionsDisplay.setMap(map);
        calcRoute(here, Graf);
});
}
function NGI(){
    art = new google.maps.LatLng(53.3418283,-6.2561985);
    navigator.geolocation.getCurrentPosition(function(position){
        var here = new google.maps.LatLng(position.coords.latitude, position.coords.longitude); 
        directionsDisplay.setMap(map);
        calcRoute(here, art);
});
}

// Here is the calculation function that creates the path on the map between the user and the destination 
function calcRoute(start,destination){
    let request = {
        origin: start, //lat lng of user
        destination: destination,
        travelMode: google.maps.TravelMode.TRANSIT,
        transitOptions: {
            modes: ['BUS'],
            routingPreference: 'FEWER_TRANSFERS'
        },
    };
    directionsService.route(request, function(response, status){
        if(status == 'OK'){
            directionsDisplay.setDirections(response);
                start_marker = new google.maps.Marker({
                position: start,
                map: map,
     
            });
                end_marker = new google.maps.Marker({
                position: destination,
                map: map,
             
            });
        }
    })

}
// Progress bar 
