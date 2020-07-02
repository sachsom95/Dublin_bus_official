let buses = {}

$( "#submit" ).click(function() {
    let x = 0;
    console.log(route)
    for (i=0; i<route[0]['steps'].length;i++){
        if (route[0]['steps'][i]['travel_mode'] == "TRANSIT"){
            buses[x] = route[0]['steps'][i]['transit']['line']['short_name'];
            console.log(route[0]['steps'][i]['transit']['line']['lat_lngs'])
            x += 1;
        }   
    }
    // $.ajax({
    //     url: '/prediction/',
    //     type: 'GET',
    //     data: buses,
    //     success: function (data) {
    //         alert(data.response);
    //     }

    // })

});

