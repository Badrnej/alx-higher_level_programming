#!/usr/bin/node
const times = process.argv;
const words = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

if (times.length <= 2) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < times[2]; i++) {
    console.log(words[0]);
  }
}
