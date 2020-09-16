#!/usr/bin/node
// script that computes and prints a factorial.

function factorial (num) {
  if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const num = parseInt(process.argv[2]);

if (num > 0) {
  const result = factorial(parseInt(num));
  console.log(result);
} else {
  console.log(1);
}
