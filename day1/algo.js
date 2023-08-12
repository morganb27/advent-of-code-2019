const fs = require('fs');

function read_file(file_path) {
    const content = fs.readFileSync(file_path, 'utf-8');
    const lines = content.split("\n");
    return lines.map(Number);
}

const file_path = 'input.txt';
const data = read_file(file_path);

function sumOfFuelRequirements() {
    let fuelRequiements = 0;
    for (let i=0; i < data.length; i++) {
        fuelRequiements += Math.floor(data[i] / 3) - 2;
    }
    return fuelRequiements
}

function sumOfFuelRequirementsAdvanced() {
    let totalFuel = 0;
    for (let i=0; i < data.length; i++) {
        moduleFuel = Math.floor(data[i] / 3) - 2;
        while(moduleFuel>0) {
            totalFuel += moduleFuel;
            moduleFuel = Math.floor(moduleFuel/3) - 2;
        }
    } 
    return totalFuel
}

console.log(sumOfFuelRequirements());
console.log(sumOfFuelRequirementsAdvanced())