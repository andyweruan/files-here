// Paste the helpful function here:
function addListItem(text){
  var list = document.querySelector('ul');
  var item = document.createElement('li');
  item.innerText = text;
  list.appendChild(item);
}
// Now use the function to add elements to the list!
//addListItem("Hi, I'm new.");

///////above is javascript

//jquery
function addListItemJQuery(itemcontent) {
  //var list = $("ul");
  //var item = document.createElement('li');
  //item.innerText = text;
  //list.append(item); //jq has in it, return own element of array w/ own functions

  $("ul").append($("<li>").text(itemcontent));
}

addListItemJQuery("Created with JQuery.");
