#!/usr/bin/node

const request = require('request');

// Get the movie ID from the first positional argument
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

// Define the API endpoint for the film
const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make a request to the film endpoint
request(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the response body
  const filmData = JSON.parse(body);

  // Get the characters list
  const characters = filmData.characters;

  // Loop through each character URL and make a request to get the name
  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }

      // Parse the character response body
      const characterData = JSON.parse(charBody);

      // Print the character name
      console.log(characterData.name);
    });
  });
});
