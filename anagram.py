'''3. Anagram Checker
 
   * Function checks if two words are anagrams.
   * Input: `"listen", "silent"`
   * Output: `True`'''

def anagram(in1,in2):
    
    in1=in1.replace(" ", "").lower()
    in2=in2.replace(" ", "").lower()
    return sorted(in1)==sorted(in2)
in1=input("enter 1st string:")
in2=input("enter 2nd string: ")
print(anagram(in1,in2))