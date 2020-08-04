var dest_name;
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
                        time_prediction = parseInt(time_prediction) + parseInt(data.prediction)
                        console.log(data.prediction)
                }
        
            })
            document.getElementById('FavDestResult').innerHTML = '"' + dest_name + '"' + ' saved as favourite destination'
        }
    }

}