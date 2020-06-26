/*options contains the dublin co-ordiantes and zoom level when 
starting a map*/
var options = {
    zoom:13,
    center:{lat:53.3498,lng:-6.2603}
}
let map
function initMap(){
    //Map options
    map = new google.maps.Map(document.getElementById('map'),options)

}

function addMarker(coords) {
    //Add marker
    let marker = new google.maps.Marker({
        position: coords,
        // why create a new map object and cause reload?
        // map: new google.maps.Map(document.getElementById('map'), options),
        map:map
    });
}

