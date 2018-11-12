# This program takes advantage of two downloadable packages from the PyPI
# = 'Python Package Index': termcolor and pyfiglet.
# Notice, that these packages have to be installed first like so:
# python -m pip install termcolor
# python -m pip install pyfiglet
# It asks the user for a string to be printed and the color to be used. Then
# it makes ASCII art of the given string.
from  termcolor import colored
from  pyfiglet import figlet_format
text = input('Enter a word: ')
if len(text) > 15:
    text = 'Too long'
col = input('Select color: red, green, yellow or blue: ')
if col not in ['red', 'green', 'yellow', 'blue']:
    col = 'red'
figlet_text = figlet_format(text)
colored_text = colored(figlet_text, color = col)
print(colored_text)

