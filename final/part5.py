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
