// Returns a random integer between min (included) and max (included)
// Using Math.round() will give you a non-uniform distribution!
function getRandomIntInclusive(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

console.log(getRandomIntInclusive(2, 11));

var total = 0;

while(total < 21) {
  var card = getRandomIntInclusive(2, 11);
  console.log("You drew a " + card);
  total += card;
  console.log("You total now is " + total);
}

if (total == 21) {
  console.log("You won");
} else {
  console.log("Sorry, you bust.");
}


//Example of an output
/*
6
"You drew a 7"
"You total now is 7"
"You drew a 10"
"You total now is 17"
"You drew a 7"
"You total now is 24"
"Sorry, you bust."
*/
