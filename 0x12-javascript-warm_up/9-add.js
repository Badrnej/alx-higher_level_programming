#!/usr/bin/node
const numbers = process.argv;
const num1 = parseInt(numbers[2]);
const num2 = parseInt(numbers[3]);

if (isNaN(num1) || isNaN(num2)) {
  console.log(NaN);
} else {
  console.log(num1 + num2);
}
