    // Declare second integer, double, and String variables.
    let i2;
    let d2;
    let s2;
    // Read and save an integer, double, and String to your variables.
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/parseInt
    i2 = parseInt(readLine());
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/parseFloat
    d2 = parseFloat(readLine());
    s2 = readLine();
    // Print the sum of both integer variables on a new line.
    console.log(i + i2);
    // Print the sum of the double variables on a new line.
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed
    console.log((d + d2).toFixed(1));
    // Concatenate and print the String variables on a new line
    console.log(s + s2);
    // The 's' variable above should be printed first.