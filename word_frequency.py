'''3. Word Frequency Counter (`collections.Counter`)
 
* Input: `"cat dog cat"`
* Output: `{'cat':2,'dog':1}`'''

from collections import Counter

def word_frequency(sentence):
    words = sentence.split()  
    return dict(Counter(words))  
text = input("Enter a sentence: ")
print(word_frequency(text))
