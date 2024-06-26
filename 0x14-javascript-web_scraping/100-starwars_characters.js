#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const movieCharacters = JSON.parse(body).characters;
    movieCharacters.forEach(character => {
      request(character, function (error, response, body) {
        if (error) {
          console.error(error);
        }
        const characterName = JSON.parse(body).name;
        console.log(characterName);
      });
    });
  }
});
