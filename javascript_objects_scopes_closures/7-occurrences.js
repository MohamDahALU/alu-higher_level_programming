#!/usr/bin/node

function nbOccurences (list, searchElement) {
  return list.reduce((a, i) => i === searchElement ? a + 1 : a);
}

module.exports = { nbOccurences };
