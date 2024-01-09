#!/usr/bin/node

exports.esrever = function (list) {
  const arr = [];
  let length = list.length - 1;

  while (length >= 0) {
    arr.push(list[length]);
    length--;
  }

  return arr;
};
