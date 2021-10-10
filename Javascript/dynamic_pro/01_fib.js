// time complexity o(2^n)
// space complexity = o(n)

// const fib = (n) => {
//     if (n <== 2){
//         return 1;
//     }
//     return fib(n-2) + fib(n-1);
// }

// console.log(fib(1));
// console.log(fib(2));
// console.log(fib(3));
// console.log(fib(4));
// console.log(fib(5));


// using dynamic prgramming(memmoization)

// time complexity = o(n)
// space complexity = o(n)

const fib = (n, cache={}) => {
    if(n in cache) return cache[n]
    if(n <= 2) return 1
    cache[n] = fib(n-1, cache) + fib(n-2, cache)
    return cache[n]
}

console.log(fib(1));
console.log(fib(2));
console.log(fib(3));
console.log(fib(4));
console.log(fib(50));