#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(apiUrl, async function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const movieCharacters = JSON.parse(body).characters;
    for (const character of movieCharacters) {
      await new Promise((resolve, reject) => {
        request(character, function (error, response, body) {
          if (error) {
            console.error(error);
            reject(error);
          } else {
            const characterName = JSON.parse(body).name;
            console.log(characterName);
            resolve();
          }
        });
      }).catch(error => console.error(error));
    }
  }
});
