#!/usr/bin/node

const argc = process.argv;

if (argc.length = 3) {
  console.log('Argument found');
} else if (argc.length > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
