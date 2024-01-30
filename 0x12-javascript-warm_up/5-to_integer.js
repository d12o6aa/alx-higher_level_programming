#!/usr/bin/node

const argc = process.argv;

if (isNumber(argc))
	console.log("My number: ", Math.trunc(argc));
else
	console.log("Not a number");

function isNumber(val) {
	return val === +val;
}
