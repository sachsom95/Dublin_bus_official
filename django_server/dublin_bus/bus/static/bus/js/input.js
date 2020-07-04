
// Author: Stacy 


// This JQuery Function creates the date and time picker as well as limits the dates selectable by having the minimum date always be today.
var today = new Date();
var end = new Date('12/31/2020');
$(function () {
    $('#datetimepicker4').datetimepicker({
        minDate: today,
        maxDate: end,
        format: 'DD/MM/YY H:mm A',
})})
// This Jquery function should change the text on the show/hide menu button when pressed 
$(document).ready(function(){
  $('#ok').on('click', function () {
    var text=$('#ok').text();
      if(text === "Hide Planner"){
        $(this).html('Show Planner');
     } else{
       $(this).text('Hide Planner');
    }
});
});
// This function takes the values entered into the intputs on the index page and re prints them out. 
function myFunction() {
    var input1 = document.getElementById("searchTextField_start").value;
    var input2 = document.getElementById("searchTextField_destination").value;
    var input3 = document.getElementById("datetimepicker4").value;
    document.getElementById("test").innerHTML = "Start: " + input1; 
    document.getElementById("test2").innerHTML = "Destination: " + input2;
    document.getElementById("test3").innerHTML = "Time and date is: " + input3;
  }
  // Below is the code for the poorly fuctioning direction planner
  $('#submit-btn').click(function() {
    $('#directions').animate({
      bottom: -$("#directions").height(),
      height: '43%',
    });
  });
  $('#close').click(function() {
    $('#directions').toggle({
      bottom: '0',
      height: '0',
    });
  });
