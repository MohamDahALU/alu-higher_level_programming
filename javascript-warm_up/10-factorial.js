#!/usr/bin/node
const arg = +process.argv[2];

if (isNaN(arg)) {
  console.log(1);
} else {
  console.log(fact(arg, arg));
}

function fact (a, n) {
  if (n === 1) return a;

  return fact(a * (n - 1), n - 1);
}
