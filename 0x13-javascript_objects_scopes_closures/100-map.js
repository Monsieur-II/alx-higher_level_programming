#!/usr/bin/node

const list = require('./100-data').list;
const new_arr = list.map((x, index) => { return x * index});

console.log(list);
console.log(new_arr);
