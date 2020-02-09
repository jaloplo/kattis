const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


let lines = 0;
let counter = 0;
let result = [];

rl.on('line', (line) => {
    if(lines === 0) {
        lines = parseInt(line);
    } else {
        result.push(line.length);

        counter++;
        if(counter === lines) {
            console.log(result.join('\n'));
        }
    }
});