#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  for (let i = 0; i < list.length / 2; i++) {
    [list[i], list[list.length - i - 1]] = [list[list.length - i - 1], list[i]];
  }
  return list;
};
