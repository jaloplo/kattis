/*
# Quadrant Selection

A common problem in mathematics is to determine which quadrant a given point lies in. There are four quadrants, numbered from 1 to 4, as shown in the diagram below:

For example, the point A, which is at coordinates (12,5) lies in quadrant 1 since both its x and y values are positive, and point B lies in quadrant 2 since its x value is negative and its y value is positive.

Your job is to take a point and determine the quadrant it is in. You can assume that neither of the two coordinates will be 0.

## Input

The first line of input contains the integer x (−1000≤x≤1000;x≠0). The second line of input contains the integer y (−1000 ≤ y ≤ 1000; y ≠ 0).

## Output

Output the quadrant number (1, 2, 3 or 4) for the point (x,y).

## Example 1

Input:
10
6

Output: 
1

## Example 2

Input: 
9
-13

Output:
4

*/

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
let output = '';

rl.on('line', (line) => {

    input.push(parseInt(line));

    if(input.length > 1) {
        const x = input[0];
        const y = input[1];

        if(x > 0 && y > 0) output = 1;
        if(x < 0 && y > 0) output = 2;
        if(x < 0 && y < 0) output = 3;
        if(x > 0 && y < 0) output = 4;

        console.log(output);
    }
});