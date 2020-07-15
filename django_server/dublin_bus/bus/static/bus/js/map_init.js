let map
let markers=[];
let directionsDisplay;
let route; 
let arr;
let dep;
let i;
let stepList = [];
let text = "<ol>";
let durationList = [];



let options = {
    zoom:13,
    center:{lat:53.3498,lng:-6.2603},
    mapTypeControl:false,
}

    function initMap() {
    //Map options
        map = new google.maps.Map(document.getElementById('map'), options)

    }


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


// $(document).on('change', '#searchTextField_start, #searchTextField_destination', function () {
//     if(markers.length ===2) {
//     removeMarker();
//     }
//
// });

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
            arr = response.routes[0].legs[0].arrival_time.text;
            dep = response.routes[0].legs[0].departure_time.text;
            duration_time = response.routes[0].legs[0].steps[0].duration.text;
            route = response.routes[0].legs[0];
            // console.log("your arrival time is " + arr);
            // console.log("your departure time is " + dep);
            console.log(route);
            console.log(response);
            // console.log(duration_time);
       
            for (i=0; i < route.steps.length; i++) {
                stepList.push(route.steps[i].instructions);
                durationList.push(route.steps[i].duration.text)
                console.log(stepList);
               
            }
            
           
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
    return stepList;
}

$(document).on('change', '#searchTextField_start, #searchTextField_destination', function () {
    console.log(`came to change event :${markers.length}`)
    if(markers.length ===2)
    {
        console.log(`inside the remove marker: ${markers.length}`)
        removeMarker();
        directionsDisplay.setMap(null);

    }

});

