#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const webUrl = process.argv[2];
const filePath = process.argv[3];

request(webUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const webData = body;
    fs.writeFile(filePath, webData, 'utf8', function () {});
  }
});
