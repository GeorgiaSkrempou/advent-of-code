const fs = require('fs');

let data = fs.readFileSync('list.txt', 'utf8');
const myArray = data.split("\n");


let elfCalories = [];
let calories=0;

for (let i = 0; i < myArray.length; i++) {
    if (myArray[i] == "") {
        elfCalories.push(calories);
        calories=0;
    } else {
        calories += parseInt(myArray[i])
    }
}

console.log(Math.max.apply(null, elfCalories));


console.log(elfCalories)
elfCalories.sort();

console.log(elfCalories.slice(0))
console.log(elfCalories.slice(-3))



// [int(elf) for elf in elf_calories]

// top_elf_calories = max(elf_calories)
// print(top_elf_calories)

// elf_calories.sort()
// print(sum(elf_calories[-3:]))

