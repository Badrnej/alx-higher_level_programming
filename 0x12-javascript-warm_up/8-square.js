#!/usr/bin/node
const times = process.argv;
const cardfight = parseInt(times[2]);

if (isNaN(cardfight)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < times[2]; i++) {
    console.log('X'.repeat(times[2]));
  }
}
