// // "use strict";
// // // for let i = 1; i<=10; i++ {
// // //     console.log(i);
// // // }
// // // while (i<=5){
// // //     console.log(i);
// // // }

// // // for(let i = 1; i<=5; i++){
// // //     if (i == 3){
// // //         continue;
// // //     }
// // //     console.log(i);
// // // }

// // function greet(name){
// //     console.log("Hello " + name);
// // }

// // greet("Prangshu");
// // greet("John");  

// // function add(a, b){
// //     return(a + b);
// // }
// // let result = add(5, 10);
// // console.log(result);


// // .	Write a JavaScript function getResult(marks, passMark = 40) that returns:
// // "A" for marks >= 80
// //  "B" for marks >= 60 and below 80
// // "C" for marks >= passMark and below 60
// // "F" for marks below passMark
// // Use a function declaration, a default parameter, if/else-if/else, and return.
// // Example: getResult(72) should return "B".
// function getResult(marks, passMark = 40){
//     if(marks >= 80){
//        return "A";
//     }
//     else if(marks >= 60){
//        return "B";
//     }
//     else if(marks >= passMark){
//        return "C";
//     }
//     else{
//         return "D";
//     }
// }
// console.log(getResult(44));
// // 3.	Write a function calculateTotal(numbers) that uses a for loop to add all numbers in an array and returns the total.
// //  Then create a function getStatus(total, target = 100) that returns "Target Reached" when total >= target and "Target Not Reached" otherwise.
// // Use return rather than printing the result from inside the functions.
// //  Example: calculateTotal([20, 35, 50]) returns 105; getStatus(105) returns "Target Reached".
// let total = 0;
// function calculateTotal(numbers){
//    for(let i = 0; i < numbers.length; i++){
//       total += numbers[i]
//    }
//    return total;
// }
// function getStatus(total, target = 100){
//    if(total >= target){
//       return "Target ho gaya oyyyyy balle balle, putter partyyyyy dede"
//    }
//    else{
//       return "Target not reached, koi nai putter. Next time dum laga dena"
//    }
// }
// console.log(calculateTotal([20,35,50]));
// console.log(getStatus(616));


// ### Temperature Checker

// (DATE - 17/09/2026)

// Create a function:

// ```jsx
// checkTemperature(temperature)
// ```

// The function should return:

// - `"Cold"` if temperature is below 20
// - `"Normal"` if temperature is between 20 and 30
// - `"Hot"` if temperature is above 30

// ### Extra Challenge

// Create a variable **inside the function**:

// ```jsx
// let message = " " ;
// ```

// Use that variable to store the result before returning it.

function temprature(temp){
let jsk = "";
   if(temp<20){
      jsk = "Cold";
   }
   if(temp>20 && temp<30){
      jsk = "Normal";
   }
   if(temp>30){
      jsk = "Hot";
   }
return jsk;
}
console.log(temprature(49));




// function add(a,b){
//    console.log(a+b);
// }
// add(10,20);












