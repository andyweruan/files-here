/* You will save your code during today's demos and exercises here. */
//$('.frame').hide();
//$('.frame').show();
//$('.frame').fadeOut(5000, 'swing');
/*
$('h5').append("<br>I love pizza");
//$('h5').addClass("newColor");
$('p').animate() {
  fontSize : 40,
}, 1500, function() {
}
*/

function fadeImage() { // event handler
  $('img').fadeToggle();
}

//This is listener , listens to the click
function setup() {
  $('#android').click(fadeImage); //id use #
//$('#android').on('click', fadeImage);     this is another way of writing it.
}

//when the page loads, this tells ur listener
$(document).ready(setup);//when doc is ready, tell setup to put it in
