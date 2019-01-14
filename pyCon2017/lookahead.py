"""
Lookahead Exercises

These functions could be made using lookaheads and/or lookbehinds.

"""
import re

with open('dictionary.txt') as dict_file:
    dictionary = dict_file.read()


def have_all_vowels(dictionary=dictionary):
    """Return all words at most 9 letters long that contain all vowels."""
    rex = re.compile(r'\b(?=\w*a)(?=\w*e)(?=\w*i)(?=\w*o)(?=\w*u)(\w{1,9})\b')
    return re.findall(rex, dictionary)

def no_repeats(dictionary=dictionary):
    """Return all words with 10 or more letters and no repeating letters."""
    def all_letters_are_unique(word):
        '''Returns True if all the letters of the word are unique.'''
        seen_before = ''
        for ch in word:
            if ch in seen_before:
                return False
            else:
                seen_before += ch
        return True

    return [word for word in re.split(r'\W+', dictionary)
            if len(word) > 9 and all_letters_are_unique(word)]


def to_pig_latin(phrase):
    """Convert English phrase to Pig Latin."""
    rex1 = re.compile(r'\b([^aeiouq]*qu?)(\w+)\b')
    rex2 = re.compile(r'\b([^aeiou]+)(\w+)\b')
    pig_words = []
    for word in re.split(r'\W+', phrase):
        if word[0] in 'aeiou':
            pig_words.append(word + 'ay')
        else:
            mo1 = rex1.search(word)
            mo2 = rex2.search(word)
            if mo1:
                pig_words.append(mo1.group(2) + mo1.group(1) + 'ay')
            else:
                pig_words.append(mo2.group(2) + mo2.group(1) + 'ay')
    return ' '.join(pig_words)


def encode_ampersands(phrase):
    """HTML-encode all & characters."""


def camel_to_underscore(camel_string):
    """Convert camelCase strings to under_score."""


def get_inline_links(markdown):
    """Return a list of all inline links."""


def find_broken_links(markdown):
    """Return a list of all broken reference-style links."""


def get_markdown_links(markdown):
    """Return a list of all markdown links."""
