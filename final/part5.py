# This file contains the part 5 of the final exercises of the Python 3
# Boot Camp.
# 1. Write a function valid_parenthesis(), which takes in a string of
# parethesis and returns True if the parethesis are valid. See the testing
# section for exemples of the correct behaviour.
import re

def valid_parentheses(parens):
    regexp = re.compile(r'\(\s*\)')
    success = 1
    while success:
        print(f'Before: {parens}')
        parens, success = regexp.subn('  ', parens)
        print(f'After : {parens}')
    return not ('(' in parens) and not (')' in parens)

# Testing
#print(valid_parentheses("()")) # True
#print(valid_parentheses(")(()))")) # False
#print(valid_parentheses("(")) # False
#print(valid_parentheses("(())((()())())")) # True
#print(valid_parentheses('))((')) # False
#print(valid_parentheses('())(')) # False
#print(valid_parentheses('()()()()())()(')) # False

# 2. Write a function reverse_vowels(). It takes in a string and reverses
# the order of the vowels in it. All the other characters maintain their
# original positions. See examples in the Testing part below.
def reverse_vowels(text):

    def is_vowel(ch):
        return ch in 'aeiouyAEIOUY'

    t_list = list(text)
    vow_list = [ch for ch in text if is_vowel(ch)]
    return ''.join([c if not is_vowel(c) else vow_list.pop() for c in text])

# Testing
#print(reverse_vowels("Hello!")) # "Holle!"
#print(reverse_vowels("Tomatoes")) # "Temotaos"
#print(reverse_vowels("Reverse Vowels In A String")) # "RivArsI Vewols en e Streng"
#print(reverse_vowels("aeiou")) # "uoiea"
#print(reverse_vowels("why try, shy fly?")) # "why try, shy fly?"

# 3. Write a function three_odd_numbers(nums), which takes in a list of ints.
# It must return True if any set of 3 consecutive numbers add up to an odd sum.
def three_odd_numbers(nums):
    for start in range(0, len(nums)-2):
        if sum(nums[start:start+3]) % 2:
            return True
    return False


# Testing
#print(three_odd_numbers([1,2,3,4,5])) # True
#print(three_odd_numbers([0,-2,4,1,9,12,4,1,0])) # True
#print(three_odd_numbers([5,2,1])) # False
#print(three_odd_numbers([1,2,3,3,2])) # False

# 4. Write a function mode(), which takes in a list of integers. It returns
# the most frequent number of the list.
def mode(nums):
    frequencies = {}
    for n in nums:
        if n in frequencies.keys():
            frequencies[n] += 1
        else:
            frequencies[n] = 1
    k_of_max_val = None
    max_val = 0
    for k, v in frequencies.items():
        if v > max_val:
            max_val = v
            k_of_max_val = k
    return k_of_max_val

# Testing
#print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4])) # 4

# 5. Write a function running-average(), which returns a function. When the
# returned function is called it returns a running average of all the previous
# calls plus this one. Like so:
# rAvg = running_average()
# rAvg(10) # 10.0
# rAvg(11) # 10.5
# rAvg(12) # 11
# 
# rAvg2 = running_average()
# rAvg2(1) # 1
# rAvg2(3) # 2
#def running_average():
#    running_average.accumulator = 0
#    running_average.size = 0
#
#    def inner(number):
#        running_average.accumulator += number
#        running_average.size += 1
#        return running_average.accumulator / running_average.size
#
#    return inner


def running_average():
    accumulator = 0
    size = 0

    def inner(number):
        nonlocal accumulator
        nonlocal size
        accumulator += number
        size += 1
        return accumulator / size

    return inner


# Testing
#rAvg = running_average()
#print(rAvg(10)) # 10.0
#print(rAvg(11)) # 10.5
#print(rAvg(12)) # 11
#rAvg2 = running_average()
#print(rAvg2(1)) # 1
#print(rAvg2(3)) # 2
