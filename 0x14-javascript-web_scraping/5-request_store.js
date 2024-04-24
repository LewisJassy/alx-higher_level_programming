#!/usr/bin/node

const request = require('request');
const file = process.argv[3];
const url = process.argv[2];
const fs = require('fs');

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFile(file, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(file);
  });
});
