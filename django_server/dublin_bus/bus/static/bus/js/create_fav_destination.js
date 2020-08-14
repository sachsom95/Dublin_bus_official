// var cur_location;

function saveFavDestination(){
    let lat = document.getElementById('stop_lat').value
    let lng = document.getElementById('stop_lng').value
    if (lat == ''){
        alert('Please add a start and end location')
    }
    else{
        console.log(lat + ' ' + lng )
        dest_name = prompt("Please enter destination name (e.g Home,Work,John's house)")
        if (dest_name == '' || dest_name == null) {
            document.getElementById('FavDestResult').innerHTML = 'No route name chosen, favourite route not saved'
        }
        else{
            $.ajax({
                url: '/add_fav_destination/',
                type: 'GET',
                async: false,
                data: {'name': dest_name, 'lat': lat,'lng':lng},
                success: function (data) {
                    // console.log(data.result)
                    document.getElementById('FavDestResult').innerHTML = data.result

                }
        
            })
        }
    }

}


function routeToFavDestination(cur_location){
    // get lat and longs of chosen destination 
    let chosen_destination = document.getElementById('favDestSelect').value
    for (i in json_destinations){
        if (json_destinations[i]['fields']['name'] == chosen_destination){
            var chosen_lat = json_destinations[i]['fields']['lat']
            var chosen_lng = json_destinations[i]['fields']['lng']
        }
    }

    //remove any markers and route first
    removeMarker()
    directionsDisplay.setMap(null)

    // create route
    addMarker(cur_location['lat'],cur_location['lng'])
    addMarker(parseFloat(chosen_lat),parseFloat(chosen_lng))
    // console.log(stepList)
    setTimeout(function(){showRoutes()},100);
    setTimeout(function(){predict()},2000);
    setTimeout(function(){myFunction()},2500);
    setTimeout(function(){document.getElementById("test1").innerHTML = " Start: Your location"},2600);
    setTimeout(function(){document.getElementById("test2").innerHTML = " End: " + chosen_destination},2600);
    setTimeout(function(){ $('#directions').show({
        bottom: '-550px',
        height:'500px',
        position: 'absolute',
      });},2800)

}

function getCurLocation(){
    navigator.geolocation.getCurrentPosition(function(position){
        let pos = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
        cur_location = JSON.parse(JSON.stringify(pos));
        routeToFavDestination(cur_location)
    });
}


function deleteFavDestination(destination_name){
    console.log(destination_name)
    $.ajax({
        url: '/delete_fav_destination/',
        type: 'GET',
        async: false,
        data: {'name': destination_name},
        success: function (data) {
            // console.log(data.result)
            document.getElementById('deletion_result').innerHTML = data.result

        }

    })

}