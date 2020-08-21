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

    
// this function uses geolocation to find an approximate location of the user.
function getLocation(){
    navigator.geolocation.getCurrentPosition(function(position){
        var pos = new google.maps.LatLng(position.coords.latitude, position.coords.longitude); // this is the user's location! 
        initMap(pos); // the location is then passed to the initMap function to be found on the map! 
    });
}

//Below is the function for putting the user's location on our map. 
// function initMap(location){ 
//     map = new google.maps.Map(document.querySelector("#map"),{
//         center: location,
//         zoom: 16,
//     });
//     directionsDisplay.setMap(map);
//     calcRoute(location, destination); // this call the calcRoute function and passes the current location and desired destination to the function
// }

// These are hard coded suggestions of popular tourist destinations.
// The user can click these to get started or click directly on the map for a more personalized search.
// Code altered from the google maps API


function Search_tourist(){

    const geocoder = new google.maps.Geocoder();
    navigator.geolocation.getCurrentPosition(function(position){
        // console.log('before: '+ markers.length)
        if (markers.length > 0){
            removeMarker()
            directionsDisplay.setMap(null)
        }
        // console.log('after: '+ markers.length)

        addMarker(position.coords.latitude, position.coords.longitude)
        // console.log('added')
        // console.log(position.coords.latitude, position.coords.longitude)
        // directionsDisplay.setMap(map); 
        // console.log(there);
        // calcRoute(here, there);
    })
    geocodeAddress(geocoder, map);
    function geocodeAddress(geocoder, resultsMap) {
    const address = document.getElementById("address").value;
    geocoder.geocode({ address: address }, (results, status) => {
      if (status === "OK") {
        resultsMap.setCenter(results[0].geometry.location);
        // addMarker(results[0].geometry.location)
        there = JSON.parse(JSON.stringify(results[0].geometry.location))
        addMarker(there['lat'],there['lng'])
        // console.log(there['lat'],there['lng'])
        // new google.maps.Marker({
        //   map: resultsMap,
        //   position: results[0].geometry.location
        // });
        // setTimeout(function(){showRoutes()},200);

        setTimeout(function(){showRoutes()},500);
        setTimeout(function(){document.getElementById("test").innerHTML = " "},1000)
        document.getElementById("journey_planner_nav").click();
        setTimeout(function(){predict()},2000);
        setTimeout(function(){myFunction()},2500);
        setTimeout(function(){document.getElementById("test1").innerHTML = " Start: Your location"},2600);
        setTimeout(function(){document.getElementById("test2").innerHTML = " End: " + address},2600);
        setTimeout(function(){ $('#directions').show({
            bottom: '-550px',
            height:'500px',
            position: 'absolute',
          });},2900)
          setTimeout(function(){document.getElementById("address").value = ""},3000);

        stepList = []
        // $('.nav-tabs a[href="#journey-planner]').tab('show')
      } else {
        alert("Geocode was not successful for the following reason: " + status);
      }
   
    // var there = results[0].geometry.location;
    // console.log("hello hello hello" + resultsMap);
    // there = results[0].geometry.location;
    // console.log(geocoder);
    });
};
}

function Guinness(){
    removeMarker()
    directionsDisplay.setMap(null)
    navigator.geolocation.getCurrentPosition(function(position){
        // var here = new google.maps.LatLng(position.coords.latitude, position.coords.longitude); 
        addMarker(position.coords.latitude,position.coords.longitude)
        addMarker(53.341978,-6.2889051)
        setTimeout(function(){showRoutes()},200);
        setTimeout(function(){document.getElementById("test").innerHTML = " "},1000)
        document.getElementById("journey_planner_nav").click();
        setTimeout(function(){predict()},2000);
        setTimeout(function(){myFunction()},2500);
        setTimeout(function(){document.getElementById("test1").innerHTML = " Start: Your location"},2600);
        setTimeout(function(){document.getElementById("test2").innerHTML = " End: Guiness Storehouse"},2600);
        setTimeout(function(){ $('#directions').show({
            bottom: '-550px',
            height:'500px',
            position: 'absolute',
          });},2900)
          setTimeout(function(){document.getElementById("address").value = ""},3000);
        // calcRoute(here, GST);
        // directionsDisplay.setMap(map);
        
});
}

function Trinity(){
    removeMarker()
    directionsDisplay.setMap(null)
    navigator.geolocation.getCurrentPosition(function(position){
        // var here = new google.maps.LatLng(position.coords.latitude, position.coords.longitude); 
        addMarker(position.coords.latitude,position.coords.longitude)
        // Trin = new google.maps.LatLng(53.3437935,-6.2567656);
        addMarker(53.3437935,-6.2567656)
        setTimeout(function(){showRoutes()},200);
        setTimeout(function(){document.getElementById("test").innerHTML = " "},1000)
        document.getElementById("journey_planner_nav").click();
        setTimeout(function(){predict()},2000);
        setTimeout(function(){myFunction()},2500);
        setTimeout(function(){document.getElementById("test1").innerHTML = " Start: Your location"},2600);
        setTimeout(function(){document.getElementById("test2").innerHTML = " End: Trinity College"},2600);
        setTimeout(function(){ $('#directions').show({
            bottom: '-550px',
            height:'500px',
            position: 'absolute',
          });},2900)
          setTimeout(function(){document.getElementById("address").value = ""},3000);
        // calcRoute(here, GST);
        // directionsDisplay.setMap(map);
        
});
}
function Grafton(){
    removeMarker()
    directionsDisplay.setMap(null)
    navigator.geolocation.getCurrentPosition(function(position){
        // var here = new google.maps.LatLng(position.coords.latitude, position.coords.longitude); 
        addMarker(position.coords.latitude,position.coords.longitude)
        // Graf = new google.maps.LatLng(53.3422917,-6.2619447);
        addMarker(53.3422917,-6.2619447)
        setTimeout(function(){showRoutes()},200);
        setTimeout(function(){document.getElementById("test").innerHTML = " "},1000)
        document.getElementById("journey_planner_nav").click();
        setTimeout(function(){predict()},2000);
        setTimeout(function(){myFunction()},2500);
        setTimeout(function(){document.getElementById("test1").innerHTML = " Start: Your location"},2600);
        setTimeout(function(){document.getElementById("test2").innerHTML = " End: Grafton Street"},2600);
        setTimeout(function(){ $('#directions').show({
            bottom: '-550px',
            height:'500px',
            position: 'absolute',
        });},2900)
        setTimeout(function(){document.getElementById("address").value = ""},3000);        
});
}
function NGI(){
    removeMarker()
    directionsDisplay.setMap(null)
    navigator.geolocation.getCurrentPosition(function(position){
        // var here = new google.maps.LatLng(position.coords.latitude, position.coords.longitude); 
        addMarker(position.coords.latitude,position.coords.longitude)
        // art = new google.maps.LatLng(53.3418283,-6.2561985);
        addMarker(53.3418283,-6.2561985)
        setTimeout(function(){showRoutes()},200);
        setTimeout(function(){document.getElementById("test").innerHTML = " "},1000)
        document.getElementById("journey_planner_nav").click();
        setTimeout(function(){predict()},2000);
        setTimeout(function(){myFunction()},2500);
        setTimeout(function(){document.getElementById("test1").innerHTML = " Start: Your location"},2600);
        setTimeout(function(){document.getElementById("test2").innerHTML = " End: NGI"},2600);
        setTimeout(function(){ $('#directions').show({
            bottom: '-550px',
            height:'500px',
            position: 'absolute',
            });},2900)
            setTimeout(function(){document.getElementById("address").value = ""},3000);
        
});
}

// Here is the calculation function that creates the path on the map between the user and the destination 
// function calcRoute(start,destination){
//     let request = {
//         origin: start, //lat lng of user
//         destination: destination,
//         travelMode: google.maps.TravelMode.TRANSIT,
//         transitOptions: {
//             modes: ['BUS'],
//             routingPreference: 'FEWER_TRANSFERS'
//         },
//     };
//     directionsService.route(request, function(response, status){
//         if(status == 'OK'){
//             directionsDisplay.setDirections(response);
//                 start_marker = new google.maps.Marker({
//                 position: start,
//                 map: map,
     
//             });
//                 end_marker = new google.maps.Marker({
//                 position: destination,
//                 map: map,
             
//             });
//         }else{
//             window.alert('Directions request failed due to ' + status);
//         };
//     })

// }
// Progress bar 
