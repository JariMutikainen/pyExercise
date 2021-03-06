"""More comprehension exercises"""


def flip_dict(orig_dict):
    """Return a new dictionary that maps the original values to the keys."""
    return {v: k for k, v in orig_dict.items()} 


def get_ascii_codes(list_of_strings):
    """Return a dictionary mapping the strings to ASCII codes."""
    output_dictionary = {}
    for string_ in list_of_strings:
        output_dictionary.update({string_: [ord(ch) for ch in string_]})
    return output_dictionary


def dict_from_truple(list_of_triples):
    """Turn three-item tuples into a dictionary of two-valued tuples."""
    return { k : (v1, v2) for k, v1, v2 in list_of_triples}


def dict_from_tuple(list_of_tuples):
    """Turn multi-item tuples into a dictionary of two-valued tuples."""
    output = {}
    for tuple_ in list_of_tuples:
        output[tuple_[0]] = tuple_[1:]
    return output


def get_all_factors(set_of_numbers):
    """Return a dictionary mapping numbers to their factors."""
    def get_factors(number):
        """Get factors of the given number."""
        return [
            n
            for n in range(1, number + 1)
            if number % n == 0

        ]

    return {n: get_factors(n) for n in set_of_numbers}

# Testing
# print(flip_dict(
      # {'Python': "2015-09-15", 'Java': "2015-09-14", 'C': "2015-09-13"}))
# words = ["hello", "bye", "yes", "no", "python"]
# print(get_ascii_codes(words))
# print(dict_from_truple([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))
# print(dict_from_tuple([(1, 2, 3, 4), (5, 6, 7, 8)]))
# print(dict_from_tuple([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))
# print(get_all_factors({1, 2, 3, 4}))
# print(get_all_factors({62, 293, 314}))
