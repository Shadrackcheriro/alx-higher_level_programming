#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (Number.isNaN(number)) {
  console.log('Not a number');
} else {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
