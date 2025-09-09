'''18. Problem: Given a list, count positive, negative, and zero numbers.'''

def count_numbers(numbers):
    p = 0
    n= 0
    z = 0
    
    for num in numbers:
        if num > 0:
            p += 1
        elif num < 0:
            n += 1
        else:
            z+= 1
    
    return p, n, z

nums = [10, -5, 0, 3, -1, 0, 7]
pos, neg, zer = count_numbers(nums)
print("Positive numbers: ",pos)
print("Negative numbers: ",neg)
print("Zeroes: ",zer)
