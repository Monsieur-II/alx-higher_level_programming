#!/usr/bin/node

let firstArgument = process.argv[2];

firstArgument = Number(firstArgument);

if (isNaN(firstArgument)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < firstArgument; i++) {
    console.log('C is fun');
  }
}
