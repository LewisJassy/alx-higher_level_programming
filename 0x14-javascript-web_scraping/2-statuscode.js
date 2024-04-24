#!/usr/bin/node

const request = require('request');
const server = process.argv[2];

request(server, function (error, response, body) {
  console.error('error:', error);
  console.log('code:', response.StatusCode);
});
