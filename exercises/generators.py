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
    parsed_range = []
    for rng in ranges:
        (min, max) = rng.split('-')
        mi = int(min)
        ma = int(max) + 1 # Add 1 because range() is non-inclusive at the max
        parsed_range.extend(range(mi, ma))

    return iter(parsed_range)


def first_prime_over(num):
    """Return the first prime number over a given number."""
    def is_prime(m):
        return not any(x for x in range(2,m) if m % x == 0)

    def prime_gen(n):
        while True:
            if is_prime(n):
                yield n
            else:
                n += 1

    return next(prime_gen(num))
        
def is_anagram(in1, in2):
    """Return True if the given words are anagrams."""
    letters1 = (ch.lower() for ch in in1 if ch.isalpha())
    letters2 = (ch.lower() for ch in in2 if ch.isalpha())
    # print(sorted(letters1), ' ', sorted(letters2))

    return sorted(letters1) == sorted(letters2)

# Testing
# print(is_prime(21))
# print(is_prime(23))
# print(list(all_together([1, 2], (3, 4), "hello")))
# nums = all_together([1, 2], (3, 4))
# print(list(all_together(nums, nums)))
# print(list(interleave([1, 2, 3, 4], [5, 6, 7, 8])))
# nums = [1, 2, 3, 4]
# print(list(interleave(nums, (n**2 for n in nums))))
# print(translate("el gato esta en la casa"))
# print(parse_ranges('1-2,4-4,8-10'))
# print(parse_ranges('0-0,4-8,20-21,43-45'))
# print(first_prime_over(1000000))
# print(is_anagram("tea", "eat")) # True
# print(is_anagram("tea", "treat")) # False
# print(is_anagram("Listen", "silent")) # True
# print(is_anagram("coins kept", "in pockets")) # True
# print(is_anagram("a diet", "I'd eat")) # True



