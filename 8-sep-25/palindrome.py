'''2. Palindrome Checker
 
   * Check if a string is palindrome (ignoring spaces & case).
   * Input: `"Never odd or even"`
   * Output: `True`'''

def palindrome(str):
    str=str.replace(' ','').lower()
    new_str=str[::-1]
    if(str==new_str):
        print("True")
    else:
        print("False")
str=input("Enter a string:")
palindrome(str)
