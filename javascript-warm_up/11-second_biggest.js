#!/usr/bin/node
const args = process.argv.slice(2);

if ([0, 1].includes(args.length)) {
  console.log(0);
} else {
  console.log(Math.max(...args));
}
