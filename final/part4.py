# This is the part 3 of the final exercises of the Python 3 boot camp.
# 1. Write a function sum_up_diagonals(), which takes in a NxN matrix
# of integers and calculates the sum of all the diagonal elements from
# the upper left corner down to lower right corner AND from the lower left
# corner up to the upper right corner.

# NOTICE, THIS SOLUTION COUNTS THE MIDDLE ELEMENT OF AN ODD SIZED MATRIX
# TWICE, WHICH IS INCORRECT (IMHO). HOWEVER, THE UNIT TESTS OF THE EXERCISE
# SEEM TO EXPECT IT TO BEHAVE THAT WAY. SO I DON'T CARE EITHER.

def sum_up_diagonals(matrix):
    def pick_elements(matrx):
        '''Returns the list of the diagonal elements of matrx
           from the upper left corner down to the lower right corner
        '''
        diag_list = []
        for r, row in enumerate(matrx):
            print(r, row)
            for c, elem in enumerate(row):
                if c == r:
                    diag_list += [elem]
        return diag_list

    def reverse_matrix(matrx):
        '''Reverses the order of the rows in the matrx.'''
        return matrx[::-1]

    elements = []
    elements += pick_elements(matrix)
    elements += pick_elements(reverse_matrix(matrix))

    return sum(elements)




# Testing
#list1 = [
#  [ 1, 2 ],
#  [ 3, 4 ]
#]
# 
#print(sum_up_diagonals(list1)) # 10
#
#list2 = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
#]
# 
#print(sum_up_diagonals(list2)) # 30
# 
#list3 = [
#  [ 4, 1, 0 ],
#  [ -1, -1, 0],
#  [ 0, 0, 9]
#]
#
#print(sum_up_diagonals(list3)) # 11
#
#list4 = [
#  [ 1, 2, 3, 4 ],
#  [ 5, 6, 7, 8 ],
#  [ 9, 10, 11, 12 ],
#  [ 13, 14, 15, 16 ]
#]
# 
#print(sum_up_diagonals(list4)) # 68

# 2. Write a function min_max_key_in_dictionary(dict_), which returns a list
# of two integers: the smallest key and the largest key of that dictionary
# min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
# min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}) # [1,4]
def min_max_key_in_dictionary(dict_):
    return [min(dict_.keys()), max(dict_.keys()) ]


# Testing
#print(min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'})) # [1,10]
#print(min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"})) # [1,4]

# 3. Write a function find_greater_numbers(list_), which returns the number
# of times an integer is followed by some greater integer. Like so:
# find_greater_numbers([6,1,2,7]) -> 4 .... because ...
# The (weird) logic of this exercise is as follows:
# 1. 2>1
# 2. 7>6
# 3. 7>1
# 4. 7>2
def find_greater_numbers(ints):
    cnt = 0
    for i, val in enumerate(ints):
        #print(f'{i}: {val}, {ints[:i]}')
        # Compare val to all the values sitting before it in the list
        for n in ints[:i]:
            if val > n:
                cnt += 1
    return cnt

# Testing
#print(find_greater_numbers([1,2,3])) # 3
#print(find_greater_numbers([6,1,2,7])) # 4
#print(find_greater_numbers([5,4,3,2,1])) # 0
#print(find_greater_numbers([])) # 0

# 4. Write a function two_oldest_ages(ages), which returns the two largest
# integers in the list in the ascening order.
def two_oldest_ages(ages):
    ages.sort()
    return ages[-2:]

# Testing
#print(two_oldest_ages( [1, 2, 10, 8] )) # [8, 10]
#print(two_oldest_ages( [6,1,9,10,4] )) # [9,10]
#print(two_oldest_ages( [4,25,3,20,19,5] )) # [20,25]

# 5. Write a function is_odd_string(string), which returns True if the sum
# of the characters of the string is odd. The string consists of a-z and
# 'a' = 1, 'b' = 2, etc.
import string

def is_odd_string(text):
    alphabet = list(string.ascii_lowercase)
    alpha_dict = {k: v for v, k in enumerate(alphabet, start=1)}
    res = 0
    for ch in text:
        res += alpha_dict[ch]
    return res % 2 == 1

# Testing
#print(is_odd_string('a')) # True
#print(is_odd_string('aaaa')) # False
#print(is_odd_string('amazing')) # True
#print(is_odd_string('veryfun')) # True
#print(is_odd_string('veryfunny')) # False
