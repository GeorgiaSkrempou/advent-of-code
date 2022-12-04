const fs = require('fs');

data = fs.readFileSync('list.txt', 'utf8');

const myArray = data.split("\n");

let count = 0;

for (let i = 0; i < myArray.length; i++) {
    let nextOne = parseInt(myArray[i+1]);
    let thisOne = parseInt(myArray[i]);
    if (nextOne>thisOne) {
        count = count+1;
  }
}

console.log(count)

let slidingWindow = []

for (let i = 0; i < myArray.length; i++) {
    if (myArray[i+1] && myArray[i+2]){
        slidingWindow.push(parseInt(myArray[i])+parseInt(myArray[i+1])+parseInt(myArray[i+2]));
    } 
}

countSliding = 0;
for (let i = 0; i< slidingWindow.length; i++) {
    if (slidingWindow[i+1]>slidingWindow[i]) {
        countSliding = countSliding+1;
  }
}
console.log(countSliding)