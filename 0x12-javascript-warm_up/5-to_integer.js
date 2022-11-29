#!/usr/bin/node
const myNum = Math.floor(Number(process.argv[2]));
if (isNaN(myNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myNum}`);
}
