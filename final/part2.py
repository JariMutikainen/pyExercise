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


