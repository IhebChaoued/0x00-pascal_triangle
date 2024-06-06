#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

request.get(url, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;
    const charNames = [];
    let count = 0;

    for (let i = 0; i < characters.length; i++) {
      request.get(characters[i], (err, resp, body) => {
        if (err) {
          console.error(err);
        } else {
          const dataName = JSON.parse(body);
          charNames[i] = dataName.name;
          count++;
          if (count === characters.length) {
            charNames.forEach(name => console.log(name));
          }
        }
      });
    }
  }
});
