#!/usr/bin/node

function factorial(arg) {
	if (isNaN(arg) || arg === 1) {
		return 1;
	}

	return arg * factorial(arg - 1);
}

let firstArg = process.argv[2];
firstArg = Number(firstArg);

console.log(factorial(firstArg));
