# The task in this file is to develop doctests for all the functions, which
# were coded in the 'function exercises' section.
# To run the doctests use the command:
#
# python -m doctest -v filename.py
#

def number_compare(a,b):
    """
    Tells, which one of the two numbers is greater.

    >>> number_compare(3, 3)
    'Numbers are equal'

    """
    if a > b:
        return "First is greater"
    elif a < b:
        return "Second is greater"
    return "Numbers are equal"

#print(number_compare(5, 5))

#def last_element(i_list):
#    """
#    Returns the last element of a given list.
#    
#    >>> last_element([1, 2, 3, 4, 5])
#    5
#
#
#    """
#    if len(i_list):
#        return i_list[-1]
#    return None

#print(last_element([1, 2, 3, 4, 5]))

#def return_day(n):
#    """
#    Returns the name of the week day based on the order number.
#    >>> return_day(3)
#    'Tuesday'
# 
#    >>> return_day(8)
#    'None'
# 
#    """
# 
#    days = [
#        "None",
#        "Sunday",
#        "Monday",
#        "Tuesday",
#        "Wednesday",
#        "Thursday",
#        "Friday",
#        "Saturday"]
#    if n > 7:
#        return "None"
#    else:
#        return days[n]
# 
#print(return_day(3))


#def product(a, b):
#    """
#    This function takes in two numbers and return the product of them.
#    >>> product(4, 5)
#    20
#
#    """
#    return a * b
#
#
## Testing
#print(product(6, 5))

