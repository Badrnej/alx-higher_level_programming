#!/usr/bin/node
const fs = require('fs');

if (process.argv.length === 3) {
  fs.readFile(process.argv[2], 'utf8', function (err, data = err) {
    console.log(data);
  });
}
