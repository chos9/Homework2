SeongJin Cho (Josh)
===================

This is an implementation of algoithem that determines whether
the given integer is prime or not. It was first published by
Manindra Angrawal, Neeraj Kayal, and Nitin Saxena in 2005 in
Paper PRIMES is in P. It has two usable method: isPrime(n) and
test(). It needs to be loaded on sage since it requires euler_phi
function in sage.

Examples:

sage: isPrime(2145)
'Composite'

sage: isPrime(2^13-1)
'Prime'

The program is quite slower than I expected. Also it does not
work well with very large numbers such as $2^31 - 1$. I will 
try to optimize it as much as possible and customize it to increase
speed.
