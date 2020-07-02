<script type="text/javascript"> 
          var today = new Date();
          var end = new Date('12/31/2020');
              $(function () {
                  $('#datetimepicker4').datetimepicker({
                      minDate: today,
                      maxDate: end,
                      format: 'DD/MM/YY H:mm A',
                  })};
</script>
function myFunction() {
  var input1 = document.getElementById("searchTextField_start").value;
  var input2 = document.getElementById("searchTextField_destination").value;
  var input3 = document.getElementById("datetimepicker4").value;
  document.getElementById("test").innerHTML = "Start: " + input1 + " Destination " + input2 + " Time and date is " + input3;
}
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
<script src="https://cdn.jsdelivr.net/momentjs/2.14.1/moment.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.37/js/bootstrap-datetimepicker.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.37/css/bootstrap-datetimepicker.min.css">