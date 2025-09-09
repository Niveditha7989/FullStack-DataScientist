'''6. Problem: Find the largest number from a list of integers.'''

def largest(l):
    a=len(l)
    l.sort()
    print(l[a-1])
largest([3,5,7,1])