#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const args = process.argv.slice(2).map(Number);
  args.sort(function (a, b) { return b - a; });
  console.log(args[1]);
}
