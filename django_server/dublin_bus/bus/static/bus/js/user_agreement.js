function hide() {
  document.getElementById("leap_form_register_btn").style.display = "none";
  document.getElementById("leap_form").style.display = "none";
  document.getElementById("form_instruction").style.display = "none";
}
hide();

function show_form() {
  document.getElementById("terms_of_use").style.display = "none";
  document.getElementById("terms_of_use_btn").style.display = "none";
  document.getElementById("leap_form_register_btn").style.display = "block";
  document.getElementById("leap_form").style.display = "block";
  document.getElementById("form_instruction").style.display = "block";
}
