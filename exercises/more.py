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




def dict_from_tuple():
    """Turn multi-item tuples into a dictionary of two-valued tuples."""


def get_all_factors():
    """Return a dictionary mapping numbers to their factors."""

# Testing
# print(flip_dict(
      # {'Python': "2015-09-15", 'Java': "2015-09-14", 'C': "2015-09-13"}))
# words = ["hello", "bye", "yes", "no", "python"]
# print(get_ascii_codes(words))
# print(dict_from_truple([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))
