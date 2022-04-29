def longest_word_in(sentence):
    count = 0
    words_list = sentence.split(" ")
    for word in words_list:
        if len(word) > count:
             count = len(word)
             longest = word
    return longest 
            
print (longest_word_in("find the longest")) 
