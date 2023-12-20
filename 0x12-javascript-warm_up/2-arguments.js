#!/usr/bin/node

const { argv } = require('process');
const argc = process.argv;

if (argc.length > 2){
    console.log('Argument found');
} else {
    console.log('No argument');
}
