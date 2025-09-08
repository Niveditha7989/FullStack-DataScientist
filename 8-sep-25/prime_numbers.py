'''1. Prime Number Finder
 
   * Function that returns all prime numbers up to `n`.
   * Input: `n = 20`
   * Output: `[2, 3, 5, 7, 11, 13, 17, 19]`'''
def primes(n):
    prime=[]
    for i in range(2,n+1):
        c=0
        for j in range(1,i+1):
            if(i%j==0):
                c+=1
        if(c==2):
            prime.append(i)
    return prime
n=int(input("enter any number:"))
print(primes(n))




