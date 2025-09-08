'''5.Second Largest Number
 
* Return 2nd largest number from a list.
 
* Input: [10, 5, 20, 8]
 
* Output: 10'''

def second_largest(n):
    values = list(set(n))  
    values.sort()
    if len(values) < 2:
        return None 
    return values[-2]
print(second_largest([10, 5, 20, 8]))
