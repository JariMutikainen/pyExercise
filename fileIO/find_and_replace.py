# Define a function find_and_replace(), which takes in 3 arguments:
# a filename, a word to the found a replaced and the replacement string.
# It should like so:
# find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
# 
# THIS SOLUTION DOES NOT MANIPULATE THE INPUT FILE EVEN THOUGH
# IT WAS SUPPOSED TO DO SO.

#import re

def find_and_replace(f_name, old_word, new_word):
    with open(f_name) as fp:
        for line in fp:
            #wordlist = re.split('[^a-zA-Z0-9,.]', line)
            wordlist = line.split()
            newlist = [new_word if w == old_word else w for w in wordlist]
            newline = ' '.join(newlist)
            #print(line)
            #print(wordlist)
            #print(newlist)
            print(newline)


# Testing
find_and_replace('koe.txt', 'Alice', 'Colt')
#find_and_replace('story.txt', 'Alice', 'Colt')
