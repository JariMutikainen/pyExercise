def is_palindrome(i_string):
    """
    def is_palindrome(i_string):

    This function returns a True if the i_string is a palindrome.
    Otherwise it returns a False. Determination is case insensitive and
    the spaces in the i_string are ignored.

    Examples:

        is_palindrome('testing') # False
        is_palindrome('tacocat') # True
        is_palindrome('hannah') # True
        is_palindrome('robert') # False
        is_palindrome('amanaplanacanalpanama') # True
    """
    lower_case_string = i_string.lower() # make everything lower case
    lower_case_string = lower_case_string.replace(" ","") # remove space
    gnirts_i = "".join(reversed(lower_case_string)) # reverse string
    return lower_case_string == gnirts_i

# Testing
print(is_palindrome('testing')) # False
print(is_palindrome('tacocat')) # True
print(is_palindrome('hannah')) # True
print(is_palindrome('robert')) # False
print(is_palindrome('amanaplanacanalpanama')) # True
print(is_palindrome('a man a plan a canal panama'))
