"""
Validation Exercises

These functions return ``True`` or ``False`` depending on whether the
string passes a condition.

"""

import re

def has_vowel(string):
    """Return True iff the string contains one or more vowels."""
    return bool(re.search(r'[aeiou]', string))


def is_integer(string):
    """Return True iff the string represents a valid integer."""
    return bool(re.search(r'^[-]?[0-9]+$', string))


def is_fraction(string):
    """Return True iff the string represents a valid fraction."""
    match_obj =  re.search(r'^-?[0-9]+/([0-9]+)$', string)
    return bool(bool(match_obj) and int(match_obj.group(1)))

def is_valid_date(string):
    """Return True iff the string represents a valid YYYY-MM-DD date."""
    match_obj = re.search(r'^[0-9]{4}-([0-9]{2})-([0-9]{2})$', string)
    if bool(match_obj):
        return bool( int(match_obj.group(1)) < 13 and
                     int(match_obj.group(2)) < 32
                   )
    return False

def is_number(string):
    """Return True iff the string represents a decimal number."""
    pattern1 = re.compile(r'^-?[0-9]+\.[0-9]+$') # 5.6
    pattern2 = re.compile(r'^-?[0-9]+\.?$')      # 5 or 5.
    pattern3 = re.compile(r'^-?\.?[0-9]+$')      # .5
    mo1 = pattern1.search(string)
    mo2 = pattern2.search(string)
    mo3 = pattern3.search(string)
    return bool(mo1 or mo2 or mo3)


def is_hex_color(string):
    """Return True iff the string represents an RGB hex color code.
     The syntax is actually '#' (RR GG BB) | (R G B) """ 
    regexp = re.compile(r'(^#[a-fA-F0-9]{3}$)|(^#([a-fA-F0-9]{2}){3}$)')

    return bool(re.search(regexp, string))

