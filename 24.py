def mymap(callback, iterable):
    result = []
    for item in iterable:
        result.append(callback(item))
    return result
# Test case 1: Create a list of squares of odd numbers from 1 to n
def square(x):
    return x**2

n = 5
odd_numbers = [i for i in range(1, n+1) if i % 2 == 1]
print(mymap(square, odd_numbers))  # Output: [1, 9, 25]

# Test case 2: Given a list of words, return a list of words with ing appended to it
def add_ing(word):
    return word + 'ing'

words = ['read', 'write', 'speak']
print(mymap(add_ing, words))  # Output: ['reading', 'writing', 'speaking']

# Test case 3: Given a list of words, return a list of tuples having the word and its length
def get_length(word):
    return (word, len(word))

words = ['apple', 'banana', 'cherry']
print(mymap(get_length, words))  # Output: [('apple', 5), ('banana', 6), ('cherry', 6)]

