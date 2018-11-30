"""List comprehension exercises"""


def get_vowel_names(names):
    """Return a list containing all names given that start with a vowel."""
    vowels = 'aeiouyAEIOUY'
    return [name for name in names if name[0] in vowels]


def power_list(numbers):
    """Return a list that contains each number raised to the i-th power."""
    return [base ** exponent for exponent, base in enumerate(numbers)]

def flatten(im):
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""
    o_matrix = []
    for lst in im:
        for elem in lst:
            o_matrix.append(elem)
    return o_matrix
 

def reverse_difference(numlist):
    """Return list subtracted from the reverse of itself."""
    reversed = numlist[::-1]
    return [n-r for n, r in zip(numlist, reversed)]


def matrix_add(m1, m2):
    """Add corresponding numbers in given 2-D matrices."""
    def sum_row(r1, r2):
        """Takes in 2 rows (= tuples) and returns the sum (a list) of them 
           as calculated element by element."""
        return [e1 + e2 for e1, e2 in zip(r1, r2)]
    rows = tuple(zip(m1, m2))
    # summed_rows = []
    # for row in rows:
    #     summed_rows.append(sum_row(row[0],row[1]))
    summed_rows = [
        sum_row(row[0],row[1])
        for row in rows
    ]
    return summed_rows

def transpose():
    """Return a transposed version of given list of lists."""


def get_factors():
    """Return a list of all factors of the given number."""


def triples():
    """Return list of Pythagorean triples less than input num."""


# Testing
# print(get_vowel_names(['Jari', 'Anne', 'Minna', 'eeva']))
# print(power_list([3,4,5.4,6]))
#i_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
#print(flatten(i_matrix))
# print(reverse_difference([1, 2, 3, 4, 5]))
#print(matrix_add([[6, 6], [3, 1]], [[1, 2], [3, 4]]))
#print(matrix_add([[1, 2, 3], [4, 5, 6]], [[-1, -2, -3], [-4, -5, -6]]))
#print(matrix_add([[6, 6], [3, 1], [2,2]], [[1, 2], [3, 4], [2,2]]))

