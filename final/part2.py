# This file contains part 2 of the final exercises of the Python bootcamp.
#
# 1. Write a function titleize() which takes in a stiring of words and returns
# the same string with the 1st letter of every word capitalized.
#
# titleize('this is awesome') # "This Is Awesome"
# titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
import re

def titleize(i_string):
    i_words = i_string.split()
    o_words = []
    regexp = re.compile(r'\b([a-z])(\S+)\b')
    for word in i_words:
        match_obj = regexp.search(word)
        o_word = match_obj.group(1).upper() + match_obj.group(2)
        o_words += [o_word]

    return ' '.join(o_words)

# Testing
#print(titleize('this is awesome')) # "This Is Awesome"
#print(titleize('oNLy cAPITALIZe fIRSt')) # "ONLy CAPITALIZe FIRSt"

# 2. Write a function find_factors(), which returns a list of the factors
# of the input argument in the ascending order.
def find_factors(num):
    return [divider for divider in range(1,num + 1) if num % divider == 0]

# Testing
#print(find_factors(10)) # [1,2,5,10 ]
#print(find_factors(11)) # [1,11]
#print(find_factors(111)) # [1,3,37,111 ]
#print(find_factors(321421)) # [1,293,1097,321421 ]

# 3. Write a function includes(), which takes in a collection, a value and
# a starting index. It returns True if value is in the collection. The search
# starts at the starting index if one is provided. The collection can be
# a string, a list or a dictionary. In the case of a dictionary the starting
# index is ignored and the the value is searched among the values - not the
# keys of it. Here we have some examples:
# includes([1, 2, 3], 1) # True 
# includes([1, 2, 3], 1, 2) # False 
# includes({ 'a': 1, 'b': 2 }, 1) # True 
# includes({ 'a': 1, 'b': 2 }, 'a') # False
# includes('abcd', 'b') # True
# includes('abcd', 'e') # False
def includes(collection, value, start_index=0):
    if type(collection) in (str, list):
        return value in collection[start_index:]
    elif type(collection) == dict:
        return value in collection.values()
    else:
        raise TypeError('Unknown collection type.')

# Testing
#print(includes([1, 2, 3], 1)) # True 
#print(includes([1, 2, 3], 1, 2)) # False 
#print(includes({ 'a': 1, 'b': 2 }, 1)) # True 
#print(includes({ 'a': 1, 'b': 2 }, 'a')) # False
#print(includes('abcd', 'b')) # True
#print(includes('abcd', 'e')) # False

# 4. Write a function repeat(i_str, n), which returns the i_str repeated
# n times. Like so:
# repeat('*', 3) # '***' 
# repeat('abc', 2) # 'abcabc' 
# repeat('abc', 0) # ''
def repeat(i_str, n):
    return i_str * n

# Testing
#print(repeat('*', 3)) # '***'
#print(repeat('abc', 2)) # 'abcabc'
#print(repeat('abc', 0)) # ''

# 5. Write a function truncate(i_str, n), which returns a truncated version
# of the i_str with '...' at the end. The total length of the returned string
# must be n characters including the 3 dots at the end. See the examples below:
#
# truncate("Super cool", 2) # "Truncation must be at least 3 characters."
# truncate("Super cool", 1) # "Truncation must be at least 3 characters."
# truncate("Super cool", 0) # "Truncation must be at least 3 characters."
# truncate("Hello World", 6) # "Hel..."
# truncate("Problem solving is the best!", 10) # "Problem..."
# truncate("Another test", 12) # "Another t..."
# truncate("Woah", 4) # "W..."
# truncate("Woah", 3) # "..."
# truncate("Yo",100) # "Yo"
# truncate("Holy guacamole!", 152) # "Holy guacamole!"
def truncate(i_str, n):
    if n < 3:
        return "Truncation must be at least 3 characters."
    elif n > len(i_str):
        return i_str
    else:
        return i_str[:n-3] + '...'


    
# Testing
#print(truncate("Super cool", 2)) # "Truncation must be at least 3 characters."
#print(truncate("Super cool", 1)) # "Truncation must be at least 3 characters."
#print(truncate("Super cool", 0)) # "Truncation must be at least 3 characters."
#print(truncate("Hello World", 6)) # "Hel..."
#print(truncate("Problem solving is the best!", 10)) # "Problem..."
#print(truncate("Another test", 12)) # "Another t..."
#print(truncate("Woah", 4)) # "W..."
#print(truncate("Woah", 3)) # "..."
#print(truncate("Yo",100)) # "Yo"
#print(truncate("Holy guacamole!", 152)) # "Holy guacamole!"

