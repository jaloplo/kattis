const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const CHIKAPU = 'Chikapu';
const BASH = 'Bash';

let lines = 0;
let result = [];

rl.on('line', (line) => {
    if(0 === lines) {
        lines = parseInt(line);
    } else {
        let length = line.length;
        if(line[0] === line[line.length -1]) {
            length = length - 1;
        }

        while(line.length > 3 && line[0] === line[2] && line[1] === line[3]) {
            line = line.slice(2);
        }

        if(length % 2 === 1) {
            result.push(CHIKAPU);
        } else {
            result.push(BASH);
        }

        lines--;

        if(0 === lines) {
            console.log(result.join('\n'));
        }
    }
});