#!/usr/bin/node
// imports an array and computes a new array
const list = require('./100-data.js').list;
console.log(list);

const newList = list.map((val, idx) => val * idx);
console.log(newList);
