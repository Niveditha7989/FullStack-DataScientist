'''11. Problem: Find smallest and largest numbers from a list.'''

def largest(l):
    a=len(l)
    l.sort()
    print("Laargest number is:",l[a-1])
    print("Smallest number is:",l[0])
largest([3,5,7,1])