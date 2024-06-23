#!/usr/bin/node

const argc = process.argv;
let x = 0;
argc.forEach((val, index) => {
  x++;
});

if (x <= 2) {
  console.log('No argument');
} else if (x >= 3) {
  argc.forEach((val, index) => {
    if (index > 1 && index < 3) {
      console.log(`${val}`);
    }
  });
}
