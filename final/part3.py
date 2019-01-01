# This is the part 3 of the final exercises of the Python 3 boot camp.
# 1. Write a function sum_up_diagonals(), which takes in a NxN matrix
# of integers and calculates the sum of all the diagonal elements from
# the upper left corner down to lower right corner AND from the lower left
# corner up to the upper right corner.
def sum_up_diagonals(matrix):
    result = 0
    for row in matrix:
        for col row:
            if row == col:
                result += matrix[row][col]
    return result



# Testing
list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
print(sum_up_diagonals(list1)) # 10

#list2 = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
#]
# 
#print(sum_up_diagonals(list2)) # 30
# 
#list3 = [
#  [ 4, 1, 0 ],
#  [ -1, -1, 0],
#  [ 0, 0, 9]
#]
#
#print(sum_up_diagonals(list3)) # 11
#
#list4 = [
#  [ 1, 2, 3, 4 ],
#  [ 5, 6, 7, 8 ],
#  [ 9, 10, 11, 12 ],
#  [ 13, 14, 15, 16 ]
#]
# 
#print(sum_up_diagonals(list4)) # 68

