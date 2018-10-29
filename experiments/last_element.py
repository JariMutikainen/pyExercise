# Return the last element of a given list.
def last_element(i_list):
    """Return the last element of a given list."""
    if len(i_list):
        return i_list[-1]
    return None

print(last_element([1,2,4,67]))
print(last_element([]))


