# I'd like you to write a function that accepts two lists-of-lists of numbers
# and returns one list-of-lists with each of the corresponding numbers in the
# two given lists-of-lists added together.
# 
# It should work something like this:
# 
# >>> matrix1 = [[1, -2], [-3, 4]]
# >>> matrix2 = [[2, -1], [0, -1]]
# >>> add(matrix1, matrix2)
# [[3, -3], [-3, 3]]
# >>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
# >>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
# >>> add(matrix1, matrix2)
# [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]


def add(matrix1, matrix2):
    """
    Adds two matricies to produce a sum matrix. 
    """
    def add_two_rows(row1, row2):
        """
        Adds two lists of numbers (= two rows of a two matricies) to produce
        a sum_row like so: [1, 2, 3] + [10, 11, 12] = [11, 13, 15]
        """
        return [v1 + v2 for v1, v2 in zip(row1, row2)]

    return [add_two_rows(r1, r2) for r1, r2 in zip(matrix1, matrix2)]



# Testing
#add_two_rows([1, -2], [2, -1])
#matrix1 = [[1, -2], [-3, 4]]
#matrix2 = [[2, -1], [0, -1]]
#print(add(matrix1, matrix2))
#matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
#matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
#print(add(matrix1, matrix2))


