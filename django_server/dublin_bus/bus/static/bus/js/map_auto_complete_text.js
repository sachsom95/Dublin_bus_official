function auto_suggest_location() {

    var input_start = document.getElementById('searchTextField_start');
    var autocomplete = new google.maps.places.Autocomplete(input_start);
    autocomplete.setComponentRestrictions({'country': ['ie']});

    var input_destination = document.getElementById('searchTextField_destination');
    var autocomplete = new google.maps.places.Autocomplete(input_destination);
    autocomplete.setComponentRestrictions({'country': ['ie']});


    google.maps.event.addListener(autocomplete, 'place_changed', function () {
        var place = autocomplete.getPlace();
    });
}
//call the auto_suggest_location function when the full DOM has been loaded
google.maps.event.addDomListener(window, 'load', auto_suggest_location);