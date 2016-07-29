function handlePaintClick(event) {
  var color = getRandomColor;
  $('body').css('background-color', color);
}

function setup() {
  $('#paint').click(handlePaintClick);
  $(window).mousemove(handleMouseMove);
    //$('h1').remove();
}
$(document).ready(setup);

function getRandomColor() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function handleMouseMove(event) {
  var x = event.pageX;
  var y = event.pageY;

  var trail = $('<div>');
  /*
  trail.css('background-color', 'gray');
  trail.width(10);
  trail.height(10);
  trail.css('position', 'absolute');
  trail.css('top', y);
  trail.css('left', x);
  */

  var newCss = {
    'background-color' : 'gray',
    'position' : 'absolute',
    'top' : 'y',
    'left' : 'x'
  };
  trail.css(newCss)

  $('body').append(trail); //trail.appendTo('body');

  console.log();
}
