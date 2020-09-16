#!/usr/bin/node
// script that prints x times “C is fun”.

let i = 0;
for (; i < process.argv[2]; i++) {
  console.log('C is fun');
}
if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
}
