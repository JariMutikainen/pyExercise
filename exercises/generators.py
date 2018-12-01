"""Generator Exercises."""


def is_prime(number):
    """Return True if candidate number is prime."""
    return not any(n for n in range(2,number) if number % n == 0) 

def all_together():
    """String together all items from the given iterables."""


def interleave():
    """Return iterable of one item at a time from each list."""


def translate():
    """Return a transliterated version of the given sentence."""


def parse_ranges():
    """Return a list of numbers corresponding to number ranges in a string"""


def first_prime_over():
    """Return the first prime number over a given number."""


def is_anagram():
    """Return True if the given words are anagrams."""

# Testing
print(is_prime(21))
print(is_prime(23))
