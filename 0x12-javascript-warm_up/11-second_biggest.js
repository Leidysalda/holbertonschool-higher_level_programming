#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.

const arr = process.argv.slice(2);

arr.sort(function (a, b) {
  return b - a;
});

if (arr.length === 0 || arr.length === 1) {
  console.log(0);
} else {
  console.log(arr[1]);
}
