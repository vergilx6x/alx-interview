#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv[2]) {
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) return console.error(err);

    const characters = JSON.parse(body).characters;
    const characterPromises = characters.map(url =>
      new Promise((resolve, reject) => {
        request(url, (error, __, charBody) => {
          if (error) return reject(error);
          resolve(JSON.parse(charBody).name);
        });
      })
    );

    Promise.all(characterPromises)
      .then(names => console.log(names.join('\n')))
      .catch(console.error);
  });
}
