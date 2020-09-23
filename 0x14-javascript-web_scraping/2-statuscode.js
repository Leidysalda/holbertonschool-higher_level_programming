#!/usr/bin/node
// script that display the status code of a GET request.

const request = require('request');
const url = process.argv[2];

request.get(url).on('response', function (response) {
  console.log('code: %d', response.statusCode);
});
