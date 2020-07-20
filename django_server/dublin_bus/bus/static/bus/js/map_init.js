let map
let markers=[];
let directionsDisplay;
let route; 
let arr;
let dep;
let i;
let stepList = [];
let text= '';
let durationList = [];
let bus;
let headsign;


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
            bus = route.steps[1].transit.line.short_name;
            headsign = route.steps[1].transit.headsign;

      

            // console.log("your arrival time is " + arr);
            // console.log("your departure time is " + dep);
            console.log(route);
            console.log(response);
            console.log("Bus number: " + bus);
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

// var geo = document.getElementById("ok");
// function getLocation() {
//   if (navigator.geolocation) {
//     navigator.geolocation.getCurrentPosition(showPosition);
//   } else {
//     geo.innerHTML = "Geolocation is not supported by this browser.";
//   }
// }
// function showPosition(position) {
//   geo.innerHTML = "Latitude: " + position.coords.latitude +
//   "<br>Longitude: " + position.coords.longitude;
// }

// $(document).on('change', '#ok', '#destination', function(){
//     console.log(`hello??: ${markers.length}`)
//     if(markers.length ==2)
//     {
//         console.log(`inside the remove marker: ${markers.length}`)
//         removeMarker();
//         directionsDisplay.setMap(null);
//     }
// });

// let startLocation = `position.coords.latitude, position.coords.longitude`;
// function GetRoute() {
//     var markers = new Array();
//     var myLatLng;
 
//     //Find the current location of the user.
//     if (navigator.geolocation) {
//         navigator.geolocation.getCurrentPosition(function (p) {
//             var myLatLng = new google.maps.LatLng(p.coords.latitude, p.coords.longitude);
//             var m = {};
//             m.title = "Mudassar's location";
//             m.lat = p.coords.latitude;
//             m.lng = p.coords.longitude;
//             markers.push(m);
 
//             //Find specified address location.
//             var address = document.getElementById("searchTextField_start").value;
//             var geocoder = new google.maps.Geocoder();
//             geocoder.geocode({ 'address': address }, function (results, status) {
//                 if (status == google.maps.GeocoderStatus.OK) {
//                     m = {};
//                     m.title = address;
//                     m.lat = results[0].geometry.location.lat();
//                     m.lng = results[0].geometry.location.lng();
//                     markers.push(m);
//                     var mapOptions = {
//                         center: myLatLng,
//                         zoom: 4,
//                         mapTypeId: google.maps.MapTypeId.ROADMAP
//                     };
//                     var map = new google.maps.Map(document.getElementById("map"), mapOptions);
//                     var infoWindow = new google.maps.InfoWindow();
//                     var lat_lng = new Array();
//                     var latlngbounds = new google.maps.LatLngBounds();
 
//                     for (i = 0; i < markers.length; i++) {
//                         var data = markers[i];
//                         var myLatlng = new google.maps.LatLng(data.lat, data.lng);
//                         lat_lng.push(myLatlng);
//                         var marker = new google.maps.Marker({
//                             position: myLatlng,
//                             map: map,
//                             title: data.title
//                         });
//                         latlngbounds.extend(marker.position);
//                         (function (marker, data) {
//                             google.maps.event.addListener(marker, "click", function (e) {
//                                 infoWindow.setContent(data.title);
//                                 infoWindow.open(map, marker);
//                             });
//                         })(marker, data);
//                     }
//                     map.setCenter(latlngbounds.getCenter());
//                     map.fitBounds(latlngbounds);
 
//                     //***********ROUTING****************//
 
//                     //Initialize the Path Array.
//                     var path = new google.maps.MVCArray();
 
//                     //Initialize the Direction Service.
//                     var service = new google.maps.DirectionsService();
 
//                     //Set the Path Stroke Color.
//                     var poly = new google.maps.Polyline({ map: map, strokeColor: '#4986E7' });
 
//                     //Loop and Draw Path Route between the Points on MAP.
//                     for (var i = 0; i < lat_lng.length; i++) {
//                         if ((i + 1) < lat_lng.length) {
//                             var src = lat_lng[i];
//                             var des = lat_lng[i + 1];
//                             path.push(src);
//                             poly.setPath(path);
//                             service.route({
//                                 origin: src,
//                                 destination: des,
//                                 travelMode: google.maps.DirectionsTravelMode.DRIVING
//                             }, function (result, status) {
//                                 if (status == google.maps.DirectionsStatus.OK) {
//                                     for (var i = 0, len = result.routes[0].overview_path.length; i < len; i++) {
//                                         path.push(result.routes[0].overview_path[i]);
//                                     }
//                                 } else {
//                                     //If the location specified is invalid, show error.
//                                     alert("Invalid location for plotting route.");
//                                     window.location.href = window.location.href;
//                                 }
//                             });
//                         }
//                     }
//                 } else {
//                     alert("Request failed.")
//                 }
//             });
 
//         });
//     }
//     else {
//         alert('Geo Location feature is not supported in this browser.');
//         return;
//     }
// }
