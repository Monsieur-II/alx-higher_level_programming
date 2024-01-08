#!/usr/bin/node

if (process.argv.length <= 3) {
	console.log(0);
}
else {
	let args = process.argv.slice(2).map(Number);

args.sort().reverse();
console.log(args[1]);
}
