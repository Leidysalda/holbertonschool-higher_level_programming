#!/usr/bin/node
// function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let letCount = 0;
  for (let pos = 0; pos < list.length; pos++) {
    if (list[pos] === searchElement) {
      letCount += 1;
    }
  }
  return letCount;
};
