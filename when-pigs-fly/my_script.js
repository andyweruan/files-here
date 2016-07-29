function showWhenClicked() {
    $("#pig").show();
}

function hideWhenClicked() {
    $("#pig").hide();
}
function fadeWhenClicked() {
  $('#pig').fadeToggle();
}
function slideWhenClicked() {
  $('#pig').slideToggle();
}
function flyWhenClicked() {
  $( "#pig" ).animate({
    opacity: 0.25,
    right: "-=50",
    height: "0"
  }, 5000, function() {
    // Animation complete.
  });
}

function setup() {
    $("#showPig").click(showWhenClicked);
    $("#hidePig").click(hideWhenClicked);
    $("#fadePig").click(fadeWhenClicked);
    $("#slidePig").click(slideWhenClicked);
    $("#flyPig").click(flyWhenClicked);
}

$(document).ready(setup);
