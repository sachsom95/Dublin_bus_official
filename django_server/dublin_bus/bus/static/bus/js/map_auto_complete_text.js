/*
Author : Sachin
Purpose of File: deals with the auto predictions of locations in Dublin and get
the lat-lon of the locations stored data in hidden fields
*/

function auto_suggest_location() {
    let start;
    let stop;

    //for bounds follow co-ordinates structure as bottom-left then top-right
    let dublinBounds = new google.maps.LatLngBounds(
        new google.maps.LatLng(53.271937,  -6.409767),
        new google.maps.LatLng(53.406819, -6.063698));
    //options to restrict api to only dublin city
    options ={
        bounds: dublinBounds,
        types: ['geocode'],
        componentRestrictions: {country: 'ie'},
        strictBounds: true
    }

    //getting the id of form field to pass to autocomplete magic function
    let input_start = document.getElementById('searchTextField_start');
    let input_destination = document.getElementById('searchTextField_destination');

    let autocomplete_input_start = new google.maps.places.Autocomplete(input_start,options);
    let autocomplete_input_destination = new google.maps.places.Autocomplete(input_destination,options);

//store value in hidden fields to reterive later feels like a hax to be honest find better way
    google.maps.event.addListener(autocomplete_input_start, 'place_changed', function () {
         start = autocomplete_input_start.getPlace();
        document.getElementById('start_lat').value = start.geometry.location.lat();
        document.getElementById('start_lng').value = start.geometry.location.lng();
    });

    google.maps.event.addListener(autocomplete_input_destination, 'place_changed', function () {
         stop = autocomplete_input_destination.getPlace();
        document.getElementById('stop_lat').value = stop.geometry.location.lat();
        document.getElementById('stop_lng').value = stop.geometry.location.lng();
    });
    //



}
//call the auto_suggest_location function when the full DOM has been loaded
google.maps.event.addDomListener(window, 'load', auto_suggest_location);


