from functools import reduce

def myreduce(callback, iterable, initial=None):
    it = iter(iterable)
    if initial is None:
        value = next(it)
    else:
        value = initial
    for element in it:
        value = callback(value, element)
    return value
# Test case 1: Given a multiword name, print its first letters
def get_initials(initials, name):
    initials += name[0]
    return initials

name = 'John Smith'
print(myreduce(get_initials, name.split(), ''))  # Output: 'JS'

# Test case 2: Find the sum of first n natural numbers
def add(a, b):
    return a + b

n = 10
numbers = range(1, n+1)
print(myreduce(add, numbers))  # Output: 55

# Test case 3: Find factorial of n
def multiply(a, b):
    return a * b

n = 5
numbers = range(1, n+1)
print(myreduce(multiply, numbers, 1))  # Output: 120

