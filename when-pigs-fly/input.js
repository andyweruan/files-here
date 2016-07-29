function handleClick(e) {
  console.log(e);
  if(e.keyCode == 13) {
    var age = $('input[name = "age"]').val();
    alert("You are " + age + " years old.");
  }
}
  /*
  var age = var age = $('input[name = "age"]').val();
  console.log(age);
  alert("You are " + age + " years old.");
}
*/
function setup() {
    $("#ageField").keypress(handleClick);
}
$(document).ready(setup);
