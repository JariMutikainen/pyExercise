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
    word_list = sentence.split()
    words = {'esta': 'is', 'la': 'the', 'en': 'in',
             'gato': 'cat', 'casa': 'house', 'el': 'the'}
    # Let the 1st word decide which way to translate.
    if word_list[0] in words.keys(): 
        spanish2english = True     
    else:
        spanish2english = False     
        
    if spanish2english:
        translated_words = (words[s_word] for s_word in word_list)
        translated_sentence = ''
        for w in translated_words:
            translated_sentence += (w + ' ')
    return translated_sentence[:-1] # Strip the trailing space

def parse_ranges(ranges_string):
    """Return a list of numbers corresponding to number ranges in a string"""
    ranges = ranges_string.split(',')
    print(ranges)

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
#print(translate("el gato esta en la casa"))
parse_ranges('1-2,4-4,8-10')
parse_ranges('0-0,4-8,20-21,43-45')
