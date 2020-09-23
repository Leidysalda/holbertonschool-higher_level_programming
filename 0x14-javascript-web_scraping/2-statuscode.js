#!/usr/bin/node
// script that display the status code of a GET request.

const url = process.argv[2];
const request = require('request');

request(url, function (response) {
  console.log('code: %d', response.statusCode);
});
