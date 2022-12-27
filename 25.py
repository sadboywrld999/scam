# Test case 1: Given a list of strings, remove all strings having first character as digit
def first_char_is_not_digit(word):
    return not word[0].isdigit()

words = ['123abc', 'abc123', 'abc']
print(myfilter(first_char_is_not_digit, words))  # Output: ['abc123', 'abc']

# Test case 2: Pickup all words whose length exceeds 6
def length_exceeds_6(word):
    return len(word) > 6

words = ['abcdef', 'abcdefg', 'abcdefgh']
print(myfilter(length_exceeds_6, words))  # Output: ['abcdefg', 'abcdefgh']

# Test case 3: Find all strings in a given line of text ending with a given suffix
def ends_with_suffix(word, suffix):
    return word.endswith(suffix)

line = 'This is a line of text'
suffix = 'text'
print(myfilter(lambda x: ends_with_suffix(x, suffix), line.split()))  # Output: ['text']

