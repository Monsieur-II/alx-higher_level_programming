#!/usr/bin/node 

let firstArgument = process.argv[2];

firstArgument = Number(firstArgument);

if (isNaN(firstArgument)) {
	console.log('Not a number');
}
else {
	console.log(`My number: ${firstArgument}`);
}
