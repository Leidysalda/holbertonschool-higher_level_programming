#!/usr/bin/node
// script that reads and prints the content of a filescript that writes a string

const fs = require('fs');
const path = process.argv[2];
const datas = process.argv[3];

fs.writeFile(path, datas, 'utf8', function (err) {
  if (err) {
    return console.error(err);
  }
});
