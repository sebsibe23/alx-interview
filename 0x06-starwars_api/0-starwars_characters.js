#!/usr/bin/node

/**
 * This script fetches and displays Star Wars characters
 * based on the provided movie ID.
 *
 * @param {number} process.argv[2] - The ID of the Star Wars movie.
 */

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    try {
      const charactersURL = JSON.parse(body).characters;
      const charactersName = charactersURL.map(
        url => new Promise((resolve, reject) => {
          request(url, (promiseErr, __, charactersReqBody) => {
            if (promiseErr) {
              reject(promiseErr);
            }
            resolve(JSON.parse(charactersReqBody).name);
          });
        })
      );

      Promise.all(charactersName)
        .then(names => console.log(names.join('\n')))
        .catch(allErr => console.log(allErr));
    } catch (parseErr) {
      console.log('Error parsing JSON:', parseErr);
    }
  });
}
