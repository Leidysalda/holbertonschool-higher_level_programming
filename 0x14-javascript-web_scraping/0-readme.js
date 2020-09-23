#!/usr/bin/node
// script that reads and prints the content of a file

const fs = require('fs');

const datas = process.argv[2];

fs.readFile(datas, 'utf8', function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.log(data);
});
