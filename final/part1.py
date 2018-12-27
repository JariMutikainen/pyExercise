# This file contains a number of small exercises, which make up the final
# chapter of the Python 3 bootcamp course.
#
# 1. Write a function reverse_string(), which reverses the characters
# of the input string
def reverse_string(i_string):
    return i_string[::-1]

# Testing
#print(reverse_string('Abcdefg'))

# 2. Write a function list_check(), which returns True, if all the elements
# of the input list are lists themselves.
def list_check(i_list):
    return all(tuple(type(item) == list for item in i_list))

# Testing
#print(list_check([[1,2,3], ['Pekka', True, 12], ['a', 'b', 'c']]))
#print(list_check([7, [1,2,3], ['Pekka', True, 12], ['a', 'b', 'c']]))

# 3. Write a function remove_every_other(), which returns a list of every
# other element of the input list.
# remove_every_other([1,2,3,4,5]) # [1,3,5] 
# remove_every_other([5,1,2,4,1]) # [5,2,1]
# remove_every_other([1]) # [1] 
def remove_every_other(i_list):
    return [item for index, item in enumerate(i_list) if index % 2 == 0]

# Testing
#print(remove_every_other([1,2,3,4,5])) # [1,3,5] 
#print(remove_every_other([5,1,2,4,1])) # [5,2,1]
#print(remove_every_other([1])) # [1] 

# 4. Write a function sum_pairs(), which takes in a list and a number.
# It returns the first pair of numbers in the list, that sums up to the
# given number. Like so:
# sum_pairs([4,2,10,5,1], 6) # [4,2]
# sum_pairs([11,20,4,2,1,5], 100) # []
def sum_pairs(i_list, num):
    if len(i_list) > 1:
        for i in range(len(i_list) - 1):
            if i_list[i] + i_list[i+1] == num:
                return [ i_list[i], i_list[i+1]]

    return []

# Testing
#print(sum_pairs([4,2,10,5,1], 6)) # [4,2]
#print(sum_pairs([11,20,4,2,1,5], 100)) # []

# 5. Write a function vowel_count(), which takes in a string and returns
# a dictionary with vowels as keys and number of occurrences as values
# Like so:
# vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
# vowel_count('Elie') # {'e': 2, 'i': 1}
# vowel_count('Colt') # {'o': 1}
def vowel_count(i_string):
    o_dict = {}
    i_string = i_string.lower()
    for ch in i_string:
        if ch in 'aeiouy':
            if ch in o_dict.keys():
                o_dict[ch] += 1
            else:
                o_dict[ch] = 1
    return o_dict


# Testing
#print(vowel_count('awesome')) # {'a': 1, 'e': 2, 'o': 1}
#print(vowel_count('Elie')) # {'e': 2, 'i': 1}
#print(vowel_count('Colt')) # {'o': 1}
