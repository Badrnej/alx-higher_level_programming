#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body).results;
    let count = 0;
    for (const i in movieData) {
      for (const chr of movieData[i].characters) {
        if (chr.search('/18/') > 0) { count += 1; }
      }
    }
    console.log(count);
  }
});
