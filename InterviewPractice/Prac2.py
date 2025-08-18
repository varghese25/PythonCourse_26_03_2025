a = 10
b = 5
print( a**b%3 )

"""
Answer: 1

Detail Explanation 
Step 1: Assign values
a = 10
b = 5

Step 2: Exponentiation a ** b

a ** b means “raise a to the power of b”.
So:
 
10 ** 5 = 10 * 10 * 10 * 10 * 10 = 100000

Step 3: Modulus %
x % y gives the remainder when x is divided by y.

So:

 100000 % 3
Now divide:
3 * 33333 = 99999
Remainder = 100000 - 99999 = 1

Step 4: Print
OutPut: print(1)

----------------------------------------------------------------
Short Explanation
a ** b ->power
% -> remainder
So it prints the remainder of (10^5) ÷ 3, which is 1.
"""