'''9. Problem: Input: 1234 → Output: 10'''


n=int(input("Enter the number:"))
s = 0
while n > 0:
    s += n% 10
    n //= 10
print(s)
