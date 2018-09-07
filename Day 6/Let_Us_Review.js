function processData(input) {
    //Enter your code here
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split
    let arr = input.split("\n"),
        evenStr, oddStr;
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach
    arr.forEach((word) => {
        evenStr = "";
        oddStr = "";
        // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN#Description
        if (!isNaN(word))
            return;
        // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from
        Array.from(word).forEach((letter, index) => {

            if (index % 2 === 0) {
                evenStr += letter;
            } else {
                oddStr += letter;
            }

        });

        console.log(evenStr.concat(" ", oddStr));
        // console.log(evenStr + " " + oddStr); // same as above
    });
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
    processData(_input);
});