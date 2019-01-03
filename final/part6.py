# This is the part 6 of the final exercises of the Python 3 Boot Camp.

# 1. Write a function letter_counter(), which accepts a string and returns
# a function. The inner function takes in a letter and returns the number
# of times the letter appears in the string.
def letter_counter(string):
    l_string = string.lower()
    def inner(ch):
        l_ch = ch.lower()
        return l_string.count(l_ch)

    return inner

# Testing
#counter = letter_counter('Amazing')
#print(counter('a')) # 2
#print(counter('m')) # 1
#
#counter2 = letter_counter('This Is Really Fun!')
#print(counter2('i')) # 2
#print(counter2('t')) # 1

# 2. Write a function once(), which takes in a function name. It defines
# an inner function, which allows the input function to be run only once.
# all the further calls to that function must return None.
def once(fname):
    called_already = False
    def inner(*args):
        nonlocal called_already
        if called_already:
            return None
        called_already = True
        return fname(*args)
    return inner



# Testing
#def add(a,b):
    #return a+b
#
#oneAddition = once(add)
#
#print(oneAddition(2,2)) # 4
#print(oneAddition(2,2)) # None
#print(oneAddition(12,200)) # None

# 3. Write a function next_prime(), which returns a generator, which is able
# to generate an infinite sequence of prime numbers starting from 2. Like
# 2, 3, 5, 7, 11, ...
def next_prime():
    def is_a_prime_number(n):
        'Returns True, if n is a prime number'
        if n == 2:
            return True
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

    p = 2
    while True:
        if is_a_prime_number(p):
            yield p
        p += 1


# Testing
#primes = next_prime()
#print([next(primes) for i in range(25)])
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
# 71, 73, 79, 83, 89, 97]

