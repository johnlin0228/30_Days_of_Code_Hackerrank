'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}



function main() {
    let n = parseInt(readLine(), 10);
    let count = 0,
        max = 0;
    while (n > 0) {
        if (n % 2 === 1) {
            count += 1;
            if (count > max) {
                max = count;
            }
        } else {
            count = 0;
        }
        n = Math.floor(n / 2);
    }
    console.log(max);
}