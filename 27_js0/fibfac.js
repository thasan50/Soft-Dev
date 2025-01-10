//Team ChewyChupacabras: Tanzeem Hasan, Ethan Sie, Brian Liu
//SoftDev pd4
//K27 - Basic functions in JavaScript
//2025-01-07m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

//<your team's fact(n) implementation>
function fact(n) {
    // Base case: factorial of 0 or 1 is 1
    if (n === 0 || n === 1) {
        return 1;
    }
    // Recursive case: n * factorial of (n-1)
    return n * fact(n - 1);
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
console.log(fact(5));
console.log(fact(0));

//-----------------------------------------------------------------


//fib:

//<your team's fib(n) implementation>
function fibonacci(n) {
    // Base case: fibonacci(0) = 0, fibonacci(1) = 1
    if (n === 0) {
        return 0;
    } else if (n === 1) {
        return 1;
    }
    // Recursive case: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2);
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
console.log(fibonacci(5)); 
console.log(fibonacci(4)); 
console.log(fibonacci(0)); 
console.log(fibonacci(1));
//=================================================================
