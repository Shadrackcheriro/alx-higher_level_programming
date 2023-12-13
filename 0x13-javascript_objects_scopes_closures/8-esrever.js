#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (Number.isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0, str; i < number; i++) {
    str = '';
    for (let j = 0; j < number; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
