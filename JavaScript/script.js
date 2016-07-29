//single line comment
/*
 * more than one line comment
*/

function checkout(item1, item2, coupon) {
  var subtotal = item1 + item2;
  var couponAmount = subtotal * coupon;
  var total = subtotal - couponAmount;
  var taxRate = total * 0.095;
  var total = total + taxRate;
  total = total.toFixed(2);
  return total;
  //return total;
  //console.log("Total amount due is " + total);
  //return total;
}
var myTotal = checkout(50, 35, 0.25);
alert("Your total is $" + myTotal);
