const fs = require('fs');

data = fs.readFileSync('list.txt', 'utf8');

let myArray = data.split("\n");

forward = 0;
up = 0;
down = 0;

for (let i = 0; i < myArray.length; i++) {
    splitLine = myArray[i].split(" ");
    if (splitLine[0] == 'forward') {
        forward = forward + parseInt(splitLine[1]);
    } else if (splitLine[0] == 'up') {
        up = up + parseInt(splitLine[1]);
    } else if (splitLine[0] == 'down') {
        down = down + parseInt(splitLine[1]);
    }
}

depth = down-up;
console.log(depth*forward);

forward = 0;
aim = 0;
depth = 0;

for (let i = 0; i < myArray.length; i++) {
    splitLine = myArray[i].split(" ");
    if (splitLine[0] == 'down') {
        aim = aim + parseInt(splitLine[1]);
    } else if (splitLine[0] == 'up') {
        aim = aim - parseInt(splitLine[1]);
    } else if (splitLine[0] == 'forward') {
        forward = forward + parseInt(splitLine[1]);
        depth = depth + (parseInt(splitLine[1])*aim);
    } 
}

console.log(depth*forward);


