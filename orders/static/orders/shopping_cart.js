//Function to disable the button when all is empty
document.addEventListener('DOMContentLoaded', () => {
  const cart_button = document.getElementById('shopping_cart');

  //Set count variable
  var count = 0;

  //Cycle through all the inputs to see if they have value
  //And monitor the inputs for changes.
  //As soon as any of the inputs are full, enable button
  //Else, disable it
  document.querySelectorAll('input').forEach(input => {
    //Find current value of count by cycling through all the initial input values
    if (input.value != "") {count += parseInt(input.value);}

    //Set the status of the button
    if(count==0){cart_button.disabled = true;}
    else{cart_button.disabled = false;}

    //When there's an input, change the count and the button accordingly
    input.addEventListener("change", () => {
      //Reset count for fresh tally
      count = 0;

      //Tally all the inputs
      document.querySelectorAll('input').forEach(input => {
        if (input.value != "") {count += parseInt(input.value);}
      });

      //Set the status of the button
      if(count==0){cart_button.disabled = true;}
      else{cart_button.disabled = false;}
    });
  });

  //When button is pressed, reset the shopping_cart value
  cart_button.onclick = (() => {
    //Create variable to store current cart
    var current_cart = [];

    //Populate that variable
    document.querySelectorAll('input').forEach(input => {
      //Select for those items that have a quantity
      if (input.value != "" || input.value != "") {
        //Add their information to the current_cart
        var item = {
          "Category": input.dataset.category,
          "Item": input.dataset.item,
          "Quantity": parseInt(input.value),
        };
        current_cart.push(item);
      }
    });
    //Store the variable
    localStorage.setItem('shopping_cart', current_cart);
  });
});
