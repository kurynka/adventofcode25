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

let dial = 50
let counter = 0

function rotating(arr) {
    for (let i = 0; i < arr.length; i++) {

        let [float, floatSign] = getFloat(arr[i])

        let new_hits = 0;
        let steps = float
        let dial_start = dial

        if (Math.abs(float) >= 100) {
            // get number of whole revolutions, e.g. 824 or -824 gives 8 here
            let integer = String(Math.abs(float))[0]
            counter = counter + Number(integer)
            new_hits = Number(integer);
            float = float % 100 // 824 gives 24 as the dial turn

            if (floatSign == true) {
                dial = dial + float
            } else {
                dial = dial + float
            }
        } else {
            dial = dial + float
        }

        //need to wrap to 0-99 and every time we wrap we can add 1 to counter
        if (dial > 99) {//we have crossed 100
            if (dial == 100) {counter++; new_hits++}
            dial = dial % 100
            if (dial != 0 && dial_start != 0) {
                counter++
                new_hits++;
                // console.log(arr[i], ' - crossed 100, old:', dial_start, 'move by:', float, 'start:', dial)
            } // else {
            //     console.log('Missta logga', arr[i], 'old:', dial_start, 'move by:', float, 'start:', dial)
            // }
        }
        else if (dial < 0) {
            dial = dial + 100
            if (dial_start != 0) {
                counter++;
                new_hits++;
                // console.log(arr[i], ' - crossed 0, old:', dial_start, 'move by:', float, 'start:', dial)
            } // else {
            //     console.log('Missta logga', arr[i], 'old:', dial_start, 'move by:', float, 'start:', dial)
            // }
        }
        else if (dial == 0) {
            counter++;
            new_hits++;
            // console.log(arr[i], ' - were on a zero, old:', dial_start, 'move by:', float, 'start:', dial)
        }
        
        console.log(`${floatSign ? 'R' : 'L'} | dial: ${dial_start} steps: ${Math.abs(steps)} hits: ${new_hits}`); 
    }

    return counter
}

function getFloat(string) {
    let sliced = string.slice(1)
    let float = +sliced
    if (string[0] == 'R') {
        return [float, true]
    } else {
        return [-float, false]
    }
}

let cunt = rotating(rotations)
console.log(cunt)

// result 1168