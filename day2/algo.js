const fs = require('fs');

function read_file(file_path) {
    const content = fs.readFileSync(file_path, 'utf-8');
    const lines = content.split(",");
    return lines.map(Number);
}

const file_path = 'input.txt';
const data = read_file(file_path);

function Intcode(inputData) {
    const myData = [...inputData];
    let num;
    for(let i=0; i<myData.length; i+=4) {
        const firstNum = myData[i];
        const secondNum = myData[i+1];
        const thirdNum = myData[i+2];
        const fourthNum = myData[i+3];
        if (firstNum === 1) {
            num = myData[secondNum] + myData[thirdNum];
            myData[fourthNum] = num;
        } else if (firstNum === 2) {
            num = myData[secondNum] * myData[thirdNum];
            myData[fourthNum] = num;
        } else {
            return myData[0];
        }
    }
    return myData[0]

}

function IntcodeAdvanced() {
    for(let i=0; i<=99;i++) {
        for (let j=0; j<=99;j++) {
            const tempData = [...data];
            tempData[1] = i;
            tempData[2] = j;
            let output = Intcode(tempData);
            if (output=== 19690720) {
                return 100 * i + j
            }
        }
    }
}


console.log(IntcodeAdvanced());