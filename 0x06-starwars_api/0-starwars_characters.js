#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to retrieve film data');
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  const fetchCharacter = (characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else if (response.statusCode !== 200) {
          reject(new Error('Failed to retrieve character data'));
        } else {
          const character = JSON.parse(body);
          resolve(character.name);
        }
      });
    });
  };

  const promises = characters.map(fetchCharacter);

  Promise.all(promises)
    .then((names) => {
      names.forEach((name) => {
        console.log(name);
      });
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});
