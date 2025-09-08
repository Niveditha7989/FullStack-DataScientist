'''3. Unique Words Counter
 
* Return unique words in a sentence.
 
* Input: "apple banana apple orange banana"
 
* Output: {'apple':2,'banana':2,'orange':1}
 '''

def unique_words_counter(str):
    words = str.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
str = "apple banana apple orange banana"
print(unique_words_counter(str))
