"""
Search Exercises

These functions return a list of strings matching a condition.

"""


import re

with open('dictionary.txt') as dict_file:
    dictionary = dict_file.read()


def get_extension(filename):
    """Return the file extension for a full file path.
    Example usage.
    >>> get_extension('archive.zip')
    'zip'
    >>> get_extension('image.jpeg')
    'jpeg'
    >>> get_extension('index.xhtml')
    'xhtml'
    >>> get_extension('archive.tar.gz')
    'gz'
    """
    regexp = re.compile(r'\.(\w+)$')
    m = regexp.search(filename)
    return m.group(1)


def tetravocalic(dictionary=dictionary):
    """Return a list of all words that have four consecutive vowels."""
    regexp = re.compile(r'\b[a-zA-Z]*[aeiouAEIOU]{4}[a-zA-Z]*\b')
    return regexp.findall(dictionary) # findall returns a list of strings.

def hexadecimal(dictionary=dictionary):
    """Return a list of all words consisting solely of the letters A to F."""


def hexaconsonantal(dictionary=dictionary):
    """Return a list of all words with six consecutive consonants."""


def possible_words(partial_word, dictionary=dictionary):
    """
    Return possible word matches from a partial word.

    Underscores in partial words represent missing letters.  Examples:
        C_T (cat, cot, cut)
        _X_ (axe)
    """


def five_repeats(letter, dictionary=dictionary):
    """Return all words with at least five occurrences of the given letter."""


def abbreviate(phrase):
    """Return an acronym for the given phrase."""


def palindrome5(dictionary=dictionary):
    """Return a list of all five letter palindromes."""


def double_double(dictionary=dictionary):
    """
    Return words with a double repeated letter with one letter between.

    Example double double words:
    - freebee
    - assessed
    - voodoo
    """


def repeaters(dictionary=dictionary):
    """
    Return words that consist of the same letters repeated two times.

    Example double double words:
    - tutu
    - cancan
    - murmur
    """
