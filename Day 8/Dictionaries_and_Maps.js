function processData(input) {
    //Enter your code here
    let input1 = input.split('\n');
    let N = parseInt(input1[0]);
    let phonebook = [];

    for (let i = 1; i <= N; i++) {
        let inputArr = input1[i].split(' ');
        // console.log(inputArr[0]);
        // console.log(inputArr[1]);
        phonebook[inputArr[0]] = inputArr[1];
    }
    // console.log(phonebook);
    for (let i = N + 1; i < input1.length; i++) {
        let num = phonebook[input1[i]];
        if (num !== undefined) {
            console.log(input1[i] + "=" + num);
        } else {
            console.log('Not found');
        }
    }

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