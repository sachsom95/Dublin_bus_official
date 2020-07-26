
function secondsToHms(d) {
    d = Number(d);
    var h = Math.floor(d / 3600);
    var m = Math.floor(d % 3600 / 60);
    var s = Math.floor(d % 3600 % 60);

    var hDisplay = h > 0 ? h + (h == 1 ? " hour, " : " hours, ") : "";
    var mDisplay = m > 0 ? m + (m == 1 ? " minute " : " minutes ") : "";
    // var sDisplay = s > 0 ? s + (s == 1 ? " second" : " seconds") : "";
    return hDisplay + mDisplay; 
}

$( "#submit-btn" ).click(function() {
    // let x = 0;
    var time_prediction = 0
    console.log(route)
    for (i=0; i<route[0]['steps'].length;i++){
        if (route[0]['steps'][i]['travel_mode'] == "TRANSIT"){
            var line = route[0]['steps'][i]['transit']['line']['short_name'];
            var dep_lat = JSON.parse(JSON.stringify(route[0]['steps'][i]['transit']['departure_stop']['location']))['lat']
            var dep_lng = JSON.parse(JSON.stringify(route[0]['steps'][i]['transit']['departure_stop']['location']))['lng']
            // console.log(dep_lat,dep_lng)
            var arr_lat = JSON.parse(JSON.stringify(route[0]['steps'][i]['transit']['arrival_stop']['location']))['lat']
            var arr_lng = JSON.parse(JSON.stringify(route[0]['steps'][i]['transit']['arrival_stop']['location']))['lng']
            // console.log(arr_lat,arr_lng)
            var google_pred = route[0]['steps'][i]['duration']['value']
            // x += 1;

            $.ajax({
                url: '/prediction/',
                type: 'GET',
                async: false,
                data: {'line': line,'dep_lat':dep_lat,'dep_lng':dep_lng,'arr_lat':arr_lat,'arr_lng':arr_lng,'google_pred':google_pred},
                success: function (data) {
                        time_prediction = parseInt(time_prediction) + parseInt(data.prediction)
                        console.log(data.prediction)
                }
        
            })
        }
    }
    // alert('Your bus journey will take' + time_prediction + 'seconds')
    // console.log(parseInt(time_prediction))
    document.getElementById("precitionResult").innerHTML = "Your bus journey(s) will take: " + secondsToHms(time_prediction)
    // sachin: this here is for geting the sharable link
    document.getElementById("share_trip").style.visibility="visible"
});


function get_shareable_link()
{
    
    let link = window.location.href +"share/"+document.getElementById("start_lat").value+"/"+
    document.getElementById("start_lng").value+"/"+document.getElementById("stop_lat").value+"/"+document.getElementById("stop_lng").value+"/"+
    document.getElementById("searchTextField_start").value+"/"+document.getElementById("searchTextField_destination").value
    document.getElementById("link_paragraph").innerHTML = link
}


function copy_link()
{

    // copies to clipboard only works if link is secured or when in localhost
    navigator.clipboard.writeText(document.getElementById("link_paragraph").innerHTML)
}