#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];

if (!filmId) {
  console.log('Usage: ./0-starwars_char.js <filmId>');
  process.exit(1);
}

const movieUrl = `https://swapi-api.hbtn.io/api/films/${filmId}/`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const data = JSON.parse(body);

  const char = data.char;

  char.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }

      const charinfo = JSON.parse(charBody);

      console.log(charinfo.name);
    });
  });
});
