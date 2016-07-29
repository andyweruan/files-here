///////////////////Lab 1//////////////////////////
var text = "ELEPHANTBEARMOUSECOW";
var word = "MOUSE";
var beg = text.indexOf(word);
var lower = word.toLowerCase();
console.log(text.substring(0 , beg) + lower + text.substring(beg + word.length))

//////////////////Lab 2 ///////////////////
var sign = prompt("Give me some letters.");

function capFirst(str) {
  var first = str.charAt(0).toUpperCase();
  return first + str.substring(1);
}

function capLast(str) {
  var last = str.charAt(str.length - 1).toUpperCase();
  return str.substring(0, str.length - 1) + last;
}

console.log(capFirst(sign));
console.log(capLast(sign));


////////////////////////// This is the arrays///////////////////

var countries = ["Chad", "Cuba", "Iceland", "Iraq",
                "Mali", "Oman"];
countries.push("Fiji");

countries.splice(5, 0, "Iran");

countries.splice(2, 1, "Togo");

countries.push("Laos");
countries.unshift("Peru");
console.log(countries.sort());




//////////////////This is the Lab for loops///////////////////////


var animals = ["lion", "tiger", "bear", "dog", "koala", "cat", "panda", "ostrich", "pig", "racoon", "monkey", "rat"];

var count = 0;
for(var a = 0; a < animals.length; a++) {
  for(var b = 0; b < animals[a].length; b++) {
    if(animals[a].charAt(b).toLowerCase() == 'a') count++;
  }
}

console.log(count);





////////////////////// This is the object Lesson/////////////////
var person = {
  age: 21, // each properties are seperated by commas
  height: 136,
  name: "Beckula",
  mothersMadienName: "NotTelling!!",
  favoriteMovieStar: "Johnny Depp"
};
//This formatting is good.Example above.


console.log(person.mothersMadienName);



//values of objects can be operated by their names
