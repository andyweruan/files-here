function checkout(item1, item2, coupon) {
  var subtotal = item1 + item2;
  var couponAmount = subtotal * coupon;
  var total = subtotal - couponAmount;
  console.log("Total amount due is " + total);
  return total;
}

var myTotal = checkout(5, 10, 0.50);

var str = "HELLLO";
console.log(str.substring(2, 5));
console.log(str.substr(2, 3));

//Output below
/*
"Total amount due is 7.5"
"LLL"
"LLL"
*/
