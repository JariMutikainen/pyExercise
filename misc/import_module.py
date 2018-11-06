def contains_keyword(*args):
    """
    def contains_keyword(*args):

    This function accepts any number of string arguments as input.
    It returns True if at least one of the input strings is a key
    word in the python language. Otherwise it returns False.  """

    # Something wrong with the syntax highlighting down below?
    from keyword import iskeyword
    return any(iskeyword(word) for word in args)


print(contains_keyword.__doc__)

# Testing
print(contains_keyword('hello', 'good bye'))    # False
print(contains_keyword('if', 'good bye', '54')) # True


