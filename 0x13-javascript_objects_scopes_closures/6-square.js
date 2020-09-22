#!/usr/bin/node
// Class Square that defines a square and inherits from Square of 5-square.js

const Square2 = require('./5-square');

class Square extends Square2 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
