#!/usr/bin/node
// script that prints a square.

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
}

const size = process.argv[2];

for (let i = 1; i <= size; i++) {
  let row = '';
  for (let j = 1; j <= size; j++) {
    row += 'X';
  }
  console.log(row);
}
