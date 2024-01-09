#!/usr/bin/node
const dic = require('./101-data').dict;

const keys = Object.keys(dic);
const values = new Set(Object.values(dic));

let arr;
const res = {};
for (const value of values) {
  arr = [];
  for (const k of keys) {
    if (dic[k] === value) {
      arr.push(k);
    }
  }
  res[value] = arr;
}
console.log(res);
