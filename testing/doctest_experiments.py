# The task in this file is to develop doctests for all the functions, which
# were coded in the 'function exercises' section.
# To run the doctests use the command:
#
# python -m doctest -v filename.py
#
def product(a, b):
    """
    This function takes in two numbers and return the product of them.
    >>> product(4, 5)
    20

    """
    return a * b


# Testing
print(product(6, 5))

