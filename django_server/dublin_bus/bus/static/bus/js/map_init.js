/*
Author: Sachin Soman
Purpose of File: This file will be run as callback from maps api. Contains initMap() function whihc
initializes the map with default options.
addMarker function adds markers in locations given
removeMarker removes all markers from map
showRoutes will display routes on map
and last jquery is to reset the map when user enters something new in text field
Global variables : map,marker,directionDisplay
*/


//aparenlty having global variables are bad so check for improvments
let map
let markers=[];
let directionsDisplay;


// default options of map which will open at dublin with zoom of 13
let options = {
    zoom:13,
    center:{lat:53.3498,lng:-6.2603},
    mapTypeControl:false,
}

    function initMap() {
    //Map options
        map = new google.maps.Map(document.getElementById('map'), options)

    }

    // makes the markers with lat,lng inputs
    function addMarker(x,y) {
        //Add marker
        coords = {lat:x,lng:y}
        let marker = new google.maps.Marker({
             position: coords,
             map: map
        })
        markers.push(marker)
    }

    
    function removeMarker(){
        while(markers.length>0)
        {
            removed_marker = markers.pop()
            removed_marker.setMap(null)
        }
    }




function showRoutes() {
    var directionsService = new google.maps.DirectionsService;

    directionsService.route({
        // The origin is the passed in marker's position.
        origin: markers[0].position,
        // The destination is user entered address.
        destination: markers[1].position,
        travelMode: 'TRANSIT',
        transitOptions: {
            //keep this for future upgrade
            // departureTime: new Date(1337675679473),
            modes: ['BUS'],
            routingPreference: 'FEWER_TRANSFERS'
        },
        unitSystem: google.maps.UnitSystem.METRIC


    }, function(response, status) {
        if (status === google.maps.DirectionsStatus.OK) {
            directionsDisplay = new google.maps.DirectionsRenderer({
                map: map,
                directions: response,
                draggable: true,
                polylineOptions: {
                    strokeColor: 'goldenrod',
                    strokeWeight:5,
                }
            });
        } else {
            window.alert('Directions request failed due to ' + status);
        }
    });



}


// this Jquery will check if user has typed something new in text field and reset the map
$(document).on('change', '#searchTextField_start, #searchTextField_destination', function () {
    console.log(`came to change event :${markers.length}`)
    /*
    we check for marker length to be 2 this ensures that the reset will happen only after
    the initial start and stop was provided. we dont want the map to be reset just after
    entering either start or stop destination
    check for better implimentation later
    */
    if(markers.length ===2)
    {
        console.log(`inside the remove marker: ${markers.length}`)
        removeMarker();
        directionsDisplay.setMap(null);

    }

});

