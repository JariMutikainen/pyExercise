"""Generator Exercises."""


def is_prime(number):
    """Return True if candidate number is prime."""
    return not any(n for n in range(2,number) if number % n == 0) 

def all_together(*args):
    """String together all items from the given iterables."""
    return (x
            for iterable in args
            for x in iterable)   


def interleave(i1, i2):
    """Return iterable of one item at a time from each list."""
    return (n
            for pair in zip(i1, i2)
            for n in pair)

def translate(sentence):
    """Return a transliterated version of the given sentence."""
    words = {'esta': 'is', 'la': 'the', 'en': 'in',
             'gato': 'cat', 'casa': 'house', 'el': 'the'}
    return words

def parse_ranges():
    """Return a list of numbers corresponding to number ranges in a string"""


def first_prime_over():
    """Return the first prime number over a given number."""


def is_anagram():
    """Return True if the given words are anagrams."""

# Testing
# print(is_prime(21))
# print(is_prime(23))
# print(list(all_together([1, 2], (3, 4), "hello")))
# nums = all_together([1, 2], (3, 4))
# print(list(all_together(nums, nums)))
# print(list(interleave([1, 2, 3, 4], [5, 6, 7, 8])))
# nums = [1, 2, 3, 4]
# print(list(interleave(nums, (n**2 for n in nums))))
translate("el gato esta en la casa")
