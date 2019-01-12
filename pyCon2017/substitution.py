"""
Substitution Exercises

These functions return a new altered version of the given string.

"""
import re

def get_extension(filename):
    """Return the file extension for a full file path."""


def normalize_jpeg(filename):
    """Return the filename with jpeg extensions normalized."""
    return re.sub(r'\.(jpeg|jpg)$', '.jpg', filename, flags=re.IGNORECASE)


def normalize_whitespace(string):
    """Replace all runs of whitespace with a single space."""
    return re.sub(r'\s+', ' ', string)


def compress_blank_lines(string, max_blanks):
    """Compress N or more empty lines into just N empty lines."""

#print(compress_blank_lines("a\n\n\n\nb\n\n\nc", max_blanks=2))


def normalize_domain(string):
    """Normalize all instances of treyhunner.com URLs."""
    exp = re.compile(r'(http://treyhunner.com)|(http://www.treyhunner.com)')
    return re.sub(exp, 'https://treyhunner.com', string)


def convert_linebreaks(string):
    """Convert linebreaks to HTML."""
    paragraphs = re.split(r'\n{2,}', string)
    o_string = ''
    for text in paragraphs:
        o_string = o_string + '<p>' + re.sub(r'\n', '<br>', text) + '</p>'
    return o_string

