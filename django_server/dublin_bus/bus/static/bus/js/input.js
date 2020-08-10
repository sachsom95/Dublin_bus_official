// src="{% static 'bus/js/map_init.js' %}"

// Author: Stacy
// This JQuery Function creates the date and time picker as well as limits the dates selectable by having the minimum date always be today.

$(document).ready(function () {
  var today = new Date();
  var end = moment(today).add(6, "M");
  $("#datetimepicker4").datetimepicker({
    minDate: today,
    maxDate: end,
    format: "DD/MM/YY LT",
    date: moment(),
    enabledHours: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    icons: {
      time: "far fa-clock",
      date: "fa fa-calendar",
      up: "fa fa-angle-up",
      down: "fa fa-angle-down",
      previous: "fa fa-angle-left",
      next: "fa fa-angle-right",
      today: "fa fa-dot-circle-o",
      clear: "fa fa-trash",
      close: "fa fa-times",
    },
  });
});
// This Jquery function should change the text on the show/hide menu button when pressed
$(document).ready(function () {
  $("#JP-btn").click(function () {
    $("#floating-panel").toggle();
    if ($("#floating-panel").is(":visible")) {
      $(this).html("Hide Planner");
    } else {
      $(this).html("Show Planner");
    }
  });
});
$(document).ready(function () {
  $("#tourist-btn").click(function () {
    $("#tourism-card").toggle();
    if ($("#tourism-card").is(":visible")) {
      $(this).html("Hide");
    } else {
      $(this).html("Show");
    }
  });
});

// This function takes the values entered into the intputs on the index page and re prints them out.
function stepListBuilder() {
  // console.log("event:7")
  // console.log("came to stepListBuilder and stepList.length is"+stepList.length)
  for (i = 0; i < stepList.length; i++ && counter <= stepList.length) {
    if (prediction_steps[i + 1] == 0) {
      text +=
        "<ul class='list-group'><li class='list-group-item'>" +
        "<span class='badge badge-primary badge-pill'>" +
        "Step: " +
        counter +
        "</span>" +
        " " +
        stepList[i] +
        " " +
        "(Duration: " +
        durationList[i] +
        ")" +
        "</li></ul>";
    } else {
      text +=
        "<ul class='list-group'><li class='list-group-item'>" +
        "<span class='badge badge-primary badge-pill'>" +
        "Step: " +
        counter +
        "</span>" +
        " " +
        stepList[i] +
        " " +
        "(Duration: " +
        prediction_steps[i + 1] +
        ")" +
        "</li></ul>";
    }
    counter += 1;
  }
  // stepList = [];
  // removeMarker();
  // directionsDisplay.setMap(null);
  // showRoutes();
}

function myFunction() {
  // console.log("event:6")
  text = ""; //start with an empty list each time
  counter = 1; //start with counter at 1 each time
  var input1 = document.getElementById("searchTextField_start").value;
  // console.log(input1)
  var input2 = document.getElementById("searchTextField_destination").value;
  // setTimeout(function(){pred_steps = prediction_steps},100);
  // console.log(pred_steps)
  // console.log(line)
  // console.log("----------stepList-----------")
  // console.log(stepList)
  // stepListBuilder();
  setTimeout(function () {
    stepListBuilder();
  }, 10);
  // console.log(stepList)

  // document.getElementById("test").innerHTML = ' ';
  // document.getElementById("test1").innerHTML = " Start: " + input1;
  // document.getElementById("test2").innerHTML = " Destination: " + input2;
  // document.getElementById("test").innerHTML = text;
  setTimeout(function () {
    document.getElementById("test").innerHTML = " ";
  }, 20);
  setTimeout(function () {
    document.getElementById("test1").innerHTML = " Start: " + input1;
  }, 20);
  setTimeout(function () {
    document.getElementById("test2").innerHTML = " Destination: " + input2;
  }, 20);
  setTimeout(function () {
    document.getElementById("test").innerHTML = text;
  }, 20);
  // document.getElementById("busbus").innerHTML = "Suggested Bus: " + bus + " towards " + headsign;
}

// Below is the code for the direction planner
//first we show the planner
$("#submit-btn").click(function () {
  $("#directions").show({
    bottom: "-550px",
    height: "500px",
    position: "absolute",
  });
});
//then we can close the planner
$("#close").click(function () {
  $("#directions").hide();
});
//then we can animate the planner each time!
$("#submit-btn").click(function () {
  $("#directions").animate({
    bottom: "-550px",
    height: "500px",
    position: "absolute",
  });
});
// this is for the tourist panel
//first we show the planner
//   $('#').click(function(){
//     $('#tourism-directions').show({
//       bottom: '-550px',
//       height:'500px',
//       position: 'absolute',
//     });
//   });
//   //then we can close the planner
//  $("#close-tourism").click(function(){
//     $("#tourism-directions").hide();
//   });
//   //then we can animate the planner each time!
//   $('#').click(function() {
//     $('#tourism-directions').animate({
//       bottom: '-550px',
//       height: '500px',
//       position: 'absolute',
//     });
//   });
