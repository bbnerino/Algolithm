def count_vowels(word):
    word = word.lower()
    result = 0
    vowels ='aeiou'
    for char in vowels:
        result += word.count(char)
    return result