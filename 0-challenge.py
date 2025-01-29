"""
Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
"""
def LongestWord(sen):
    'finds the longest word'
    previous_length = 0
    longest_word = ''
    for word in sen.split(' '):
        word = remove_punctation(word)
        if previous_length <  len(word):
            longest_word = word
            previous_length = len(word)
    return longest_word

def remove_punctation(word):
    'removes punctuation marks in a word'
    new_word = ''
    for char in word:
        if char.isalnum():
            new_word += char
    return new_word
    
print(LongestWord(input()))
