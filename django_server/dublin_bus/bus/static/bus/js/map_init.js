

let options = {
    zoom:13,
    center:{lat:53.3498,lng:-6.2603},
    mapTypeControl:false,
}

let map
function initMap() {
    //Map options
    map = new google.maps.Map(document.getElementById('map'), options)

}

let markers=[];

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


$(document).on('change', '#searchTextField_start, #searchTextField_destination', function () {
    if(markers.length ===2) {
    removeMarker();
    }
});

