#!/usr/bin/node

const args = process.argv;

const number = parseInt(args[2]);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
