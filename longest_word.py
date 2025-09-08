'''5. Longest Word Finder
 
* Return longest word in a sentence.
* Input: `"Python is amazing"`
* Output: `"amazing"`'''

def longest_word(str):
    words=str.split(' ')
    longest=''
    for i in words:
        if(len(i)>len(longest)):
            longest=i
    return longest
str=input("Enter a sentence:")
long=longest_word(str)
print(long)