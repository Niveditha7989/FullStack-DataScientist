'''13. Problem: Input 3 numbers, print the largest.'''

def largest(l):
    if len(l)>3:
        print("enter only 3 numbers")
    else:
        l.sort()
        print("largest:",l[-1])
largest([1,10,3])