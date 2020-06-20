var options = {
    zoom:13,
    center:{lat:53.3498,lng:-6.2603}
}

function initMap(){
    //Map options
    var map = new google.maps.Map(document.getElementById('map'),options)

}

function addMarker(coords) {
    //Add marker
    var marker = new google.maps.Marker({
        position: coords,
        map: new google.maps.Map(document.getElementById('map'), options),
        icon: 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'

    });
}