def multiple_letter_count(word):
    """Counts the number of occurrences of each character in the input string.
    """
    return {ch : word.count(ch) for ch in word}

word = 'awesome'
print(multiple_letter_count(word))
print(multiple_letter_count.__doc__)


