#!/usr/bin/node
const numbers = process.argv;
const num1 = parseInt(numbers[2]);

function fact (number) {
  if (number === 0 || isNaN(number)) {
    return (1);
  }
  return (number * fact(number - 1));
}

console.log(fact(num1));
