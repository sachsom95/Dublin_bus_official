
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

$( "#submit" ).click(function() {
    // let x = 0;
    var time_prediction = 0
    console.log(route)
    // get an array with the number of hours and minutes chosen by the user 
    let hour_minutes = document.getElementById("datetimepicker4").value.split(" ")[1].split(":");
    // create a total seconds variable with the seconds that have elapsed in the day for the prediction model
    var total_seconds = 0;
    total_seconds += hour_minutes[0] * 60 * 60
    total_seconds += hour_minutes[1] * 60
    // create a date object for prediction model
    let date = document.getElementById("datetimepicker4").value.split(" ")[0].split("/")
    let date_obj = new Date('20'+date[2],date[1]-1,date[0])
    // now all I really need from the date object is the day of the week so I will extract that
    // I actually want the string representation not an integer so I'll parse the date object as a string
    var dow = String(date_obj).split(" ")[0]
    console.log(dow)
    for (i=0; i<route[0]['steps'].length;i++){
        if (route[0]['steps'][i]['travel_mode'] == "TRANSIT"){
            // for each line get the line number and departure and arrival coordinates to pass to django
            var line = route[0]['steps'][i]['transit']['line']['short_name'];
            var dep_lat = JSON.parse(JSON.stringify(route[0]['steps'][i]['transit']['departure_stop']['location']))['lat']
            var dep_lng = JSON.parse(JSON.stringify(route[0]['steps'][i]['transit']['departure_stop']['location']))['lng']
            // console.log('line ' + line + ' departure coordinates: ' + dep_lat,dep_lng)
            var arr_lat = JSON.parse(JSON.stringify(route[0]['steps'][i]['transit']['arrival_stop']['location']))['lat']
            var arr_lng = JSON.parse(JSON.stringify(route[0]['steps'][i]['transit']['arrival_stop']['location']))['lng']
            // console.log('line ' + line + ' arrival coordinates: ' + arr_lat,arr_lng)
            // console.log(arr_lat,arr_lng)
            var google_pred = route[0]['steps'][i]['duration']['value']
            // x += 1;

            $.ajax({
                url: '/prediction/',
                type: 'GET',
                async: false,
                data: {'line': line,'dep_lat':dep_lat,'dep_lng':dep_lng,'arr_lat':arr_lat,'arr_lng':arr_lng,'google_pred':google_pred,'time':total_seconds,'day':dow},
                success: function (data) {
                        time_prediction = parseInt(time_prediction) + parseInt(data.prediction)
                        console.log(data.prediction)
                }
        
            })
        }
    }
    // alert('Your bus journey will take' + time_prediction + 'seconds')
    // console.log(parseInt(time_prediction))
    document.getElementById('precitionResult').innerHTML = "Your bus journey(s) will take: " + secondsToHms(time_prediction)

});



