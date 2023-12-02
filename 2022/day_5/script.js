const fs = require('fs');

let data = fs.readFileSync('crates.txt', 'utf8');
const myArray = data.split("\n");


let moveLines = []
for (i=10; i<myArray.length; i++) {
    moveLines.push(myArray[i]);
}

let crateLines = []
for (i=0; i<8; i++) {
    crateLines.push(myArray[i]);
}

let cratesDict = {
    1: ["G", "F", "V", "H", "P", "S"],
    2: ["G", "J", "F", "B", "V", "D", "Z", "M"],
    3: ["G", "M", "L", "J", "N"],
    4: ["N", "G", "Z", "V", "D", "W", "P"],
    5: ["V", "R", "C", "B"],
    6: ["V", "R", "S", "M", "P", "W", "L", "Z"],
    7: ["T", "H", "P"],
    8: ["Q", "R", "S", "N", "C", "H", "Z", "V"],
    9: ["F", "L", "G", "P", "V", "Q", "J"]
  };


for (i=0; i<moveLines.length;i++) {
    let line = moveLines[i];
    let splitLine = line.split(" ");
    console.log(splitLine);
    let integerArray = [];

    for (y=0; y<splitLine.length;y++) {
        if (parseInt(splitLine[y])) {
            console.log(parseInt(splitLine[y]))
        }

        // break;
    }
    // console.log(moveLines[i])
}

// let nextOne = parseInt(myArray[i+1]);

