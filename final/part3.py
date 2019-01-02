
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

# 10. Write a function find_the_duplicate(). It takes in a list of numbers
# and returns the one, that appears in the list twice. In case there is no
# such number there, the function returns None.
# find_the_duplicate([1,2,1,4,3,12]) # 1
# find_the_duplicate([6,1,9,5,3,4,9]) # 9
# find_the_duplicate([2,1,3,4]) # None

def find_the_duplicate(lst):
    seen_before = []
    for n in lst:
        if n in seen_before:
            return n
        else:
            seen_before += [n]
    return None


# Testing
#print(find_the_duplicate([1,2,1,4,3,12])) # 1
#print(find_the_duplicate([6,1,9,5,3,4,9])) # 9
#print(find_the_duplicate([2,1,3,4])) # None
