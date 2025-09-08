'''2. Simple Calculator with `math`
 
* Perform sqrt, factorial, sin, cos.
* Input: `sqrt(25)`
* Output: `5.0`'''

import math
def square_root(n):
    return math.sqrt(n)
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
def sine(n):
    return math.sin(n)
def cose(n):
    return math.cos(n)
n=int(input("Enter number:"))
print(square_root(n))
print(factorial(n))
print(sine(n))
print(cose(n))

