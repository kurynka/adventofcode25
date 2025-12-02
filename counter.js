import { readFileSync } from 'node:fs';

// start at 50 
// range 0-99
// every time it lands on 0 we increment the counter
// this means every time we land at 0, 100, 200, -100, -200 etc we increment
// we can treat there as floats so - every time were at a whole number we increment counter

var rotations = []

var data = readFileSync('/Users/kalinka/adventofcode25/input.txt', 'utf8');

rotations = data.split('\n')

// console.log(rotations);

let start = 50
let counter = 0

function rotating(arr) {
    for (let i = 0; i < arr.length; i++) {
        let float = getFloat(arr[i])
        console.log(float)
        start = start + float
        if (start % 100 == 0) { counter++ }
    }
    console.log(start)
    return counter
}

function getFloat(string) {
    let sliced = string.slice(1)
    let float = +sliced 
    if (string[0] == 'R') { return float } else { return -float }
}

let cunt = rotating(rotations)
console.log(cunt)