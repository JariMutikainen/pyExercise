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

# 6. Write a function two_list_dictionary(), which takes in two lists:
# keys and values. Return a dictionary, which combines the two lists.
# If there are too many keys insert null for their values. If there are
# too many values, ignore the excess values.
def two_list_dictionary(keys_, values_):
    # Fill in None for the missing values.
    while len(values_) < len(keys_):
        values_ += [None]

    return {k: v for k, v in zip(keys_, values_)}

# Testing
#print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
#print(two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4])) # {'a': 1, 'b': 2, 'c': 3}
#print(two_list_dictionary(['x', 'y', 'z']  , [1,2])) # {'x': 1, 'y': 2, 'z': None}

# 7. Write a function range_in_list(), which returns the sum of list elements
# between the start and end indicies (inclusive). The default value for 
# start is 0 and the default value of end is len(i_lst) - 1.
# In case the value of end is out of range the sum must be calculated
# all the way to the last element of the list.
def range_in_list(lst, start=0,end=None):
    if end == None:
        end = len(lst)
    return sum(lst[start:end+1])

# Testing
#print(range_in_list([1,2,3,4],0,2)) #  6
#print(range_in_list([1,2,3,4],0,3)) # 10
#print(range_in_list([1,2,3,4],1)) #  9
#print(range_in_list([1,2,3,4])) # 10
#print(range_in_list([1,2,3,4],0,100)) # 10
#print(range_in_list([],0,1)) # 0

# 8. Write a function same_frequency(), which takes in two integers. It returns
# True, if both integers contain the same frequency of numbers.
# See the examples below:
# same_frequency(551122,221515) # True
# same_frequency(321142,3212215) # False
# same_frequency(1212, 2211) # True
def same_frequency(num1, num2):
    freqs1 = [0,0,0,0,0,0,0,0,0,0] 
    freqs2 = [0,0,0,0,0,0,0,0,0,0] 
    str1 = str(num1)
    str2 = str(num2)
    for ch in str1:
        freqs1[int(ch)] += 1
    for ch in str2:
        freqs2[int(ch)] += 1
    #return not cmp(freqs1, freqs2)
    return all(val1 == val2 for val1, val2 in zip(freqs1, freqs2))


# Testing
#print(same_frequency(551122,221515)) # True
#print(same_frequency(321142,3212215)) # False
#print(same_frequency(1212, 2211)) # True

# 9. Write a function nth(), which takes in a list and an index. It returns
# the element at that index. If the index is negative it returns the nth
# value starting from the end of the list.
# nth(['a', 'b', 'c', 'd'], 1)  # 'b'
# nth(['a', 'b', 'c', 'd'], -2) #  'c'
# nth(['a', 'b', 'c', 'd'], 0)  # 'a'
# nth(['a', 'b', 'c', 'd'], -4) #  'a'
# nth(['a', 'b', 'c', 'd'], -1) #  'd'
# nth(['a', 'b', 'c', 'd'], 3)  # 'd'
def nth(lst, index):
    return lst[index]

# Testing
#print(nth(['a', 'b', 'c', 'd'], 1))  # 'b'
#print(nth(['a', 'b', 'c', 'd'], -2)) #  'c'
#print(nth(['a', 'b', 'c', 'd'], 0))  # 'a'
#print(nth(['a', 'b', 'c', 'd'], -4)) #  'a'
#print(nth(['a', 'b', 'c', 'd'], -1)) #  'd'
#print(nth(['a', 'b', 'c', 'd'], 3))  # 'd'
