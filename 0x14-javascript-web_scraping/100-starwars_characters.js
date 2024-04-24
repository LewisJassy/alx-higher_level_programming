#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const movieData = JSON.parse(body);
  const characters = movieData.characters;
  characters.forEach(characterUrl => {
    request.get(characterUrl, (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
