function moveRight() {
  var position = $('#pokemon').position();
  var left = position.left;
  $('#pokemon').css('left', (left + 10));
  //alert(left);
}

function moveLeft() {
  var position = $('#pokemon').position();
  var left = position.left;
  if (left > 0) {
    $('#pokemon').css('left', (left - 10));
  }
}

function moveUp() {
  var position = $('#pokemon').position();
  var top = position.top;
  if (top > 0) {
    $('#pokemon').css('top', (top - 10));
  }
}

function moveDown() {
  var position = $('#pokemon').position();
  var top = position.top;
  if (top < 770) {
    $('#pokemon').css('top', (top + 10));
  }
}

function handleKeyPress(event) {
  console.log(event.keyCode)
  if (event.keyCode == 100) {
    moveRight();
  } else if (event.keyCode == 97) {
    moveLeft();
  } else if (event.keyCode == 119) {
    moveUp();
  } else {
    moveDown();
  }
}

function setup() {
  $(window).keypress(handleKeyPress);
}

$(document).ready(setup);
