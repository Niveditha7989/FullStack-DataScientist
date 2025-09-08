'''1. Fibonacci Generator
 
* Function generates n Fibonacci numbers.
 
* Input: n = 7
 
* Output: [0, 1, 1, 2, 3, 5, 8]'''

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq
n=int(input("Enter input number:"))
print(fibonacci(n))
