'''4. Count Vowels & Consonants
 
   * Return count of vowels & consonants.
   * Input: `"hello"`
   * Output: `Vowels=2, Consonants=3`'''

str=input("enter any string:")
vowels="aeiouAEIOU"
v=0
c=0
for char in str:
    if char.isalpha():
        if char in vowels:
            v+=1
        else:
            c+=1
print("vowels:",v,"consonants:",c)



