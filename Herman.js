const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    let radius = parseInt(line);

    console.log(Math.PI * Math.pow(radius, 2));

    let square_side = Math.sqrt(Math.pow(radius, 2) * 2);
    let area = Math.pow(square_side, 2);
    console.log(Math.round(area));
});