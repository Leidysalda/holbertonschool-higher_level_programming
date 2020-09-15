#!/usr/bin/node
// script that prints the first argument passed to it.

if (process.argv[2] != undefined){
  console.log(process.argv[2], 'is', process.argv[3]);
} else {
  console.log('undefined is', process.argv[3])
  }
