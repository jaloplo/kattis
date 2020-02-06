const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
let data = [];

function repeat(vector, row_times, column_times) {
    let output = '';
    for(let i = 0; i < vector.length; i++) {
        let text = '';
        for(let j = 0; j < vector[i].length; j++) {
            text += vector[i][j].repeat(column_times);
        }
        output += new String(text + '\n').repeat(row_times);
    }
    return output;
}

rl.on('line', (line) => {
    if(input.length === 0) {
        input = line.split(' ');
    } else {
        data.push(line);
        if(data.length === parseInt(input[0])) {
            let output = repeat(data, parseInt(input[2]), parseInt(input[3]));
            console.log(output);
        }
//     }
// });