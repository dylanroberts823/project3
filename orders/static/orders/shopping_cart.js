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
});
