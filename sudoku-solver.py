#!/usr/bin/env python

# Script for solving a sudoku problem using the backtracking algorithm

# Algorithm:

# 1. Create a function that checks after assigning the current index if the grid becomes unsafe or not. Keep Hashmap for a row, column and boxes.
# If any number has a frequency greater than 1 in the hashMap return false, else return true; hashMap can be avoided by using loops.
# 2. Create a recursive function that takes a grid.
# 3. Check for any unassigned location. If present then assign a number from 1 to 9, check if assigning the number to current index makes the
# grid unsafe or not, if safe then recursively call the function for all safe cases from 0 to 9. if any recursive call returns true, end the loop
# and return true. If no recursive call returns true then return false.
# 4. If there is no unassigned location then return true.


# code:

# function for printing the matrix:
def print_matrix(matrix):
    for line in matrix:
        for cell in line:
            print(cell, end=" ")
        print()


# function to create the full hashmap of a matrix
def create_hasmap(matrix):
    complete_dic = {
        "row": {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
        "col": {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
        "box": {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
    }

    # iterate over matrix
    # and add cell to the correct hashmap
    nrow = 0
    nbox = 0

    for row in matrix:
        # for row in sudoku_matrix:
        nrow += 1
        ncol = 0
        for cell in row:
            ncol += 1

            complete_dic["row"][nrow].append(cell)
            complete_dic["col"][ncol].append(cell)

            if nrow < 4 and ncol < 4:
                nbox = 1
            if nrow < 4 and (ncol >= 4 and ncol < 7):
                nbox = 2
            if nrow < 4 and ncol >= 7:
                nbox = 3

            if (nrow >= 4 and nrow < 7) and ncol < 4:
                nbox = 4
            if (nrow >= 4 and nrow < 7) and (ncol >= 4 and ncol < 7):
                nbox = 5
            if (nrow >= 4 and nrow < 7) and ncol >= 7:
                nbox = 6

            if nrow >= 7 and ncol < 4:
                nbox = 7
            if nrow >= 7 and (ncol >= 4 and ncol < 7):
                nbox = 8
            if nrow >= 7 and ncol >= 7:
                nbox = 9

            complete_dic["box"][nbox].append(cell)
    return complete_dic


# function to check if the matrix is a valid matrix. makes use of the create_hashmap() function
def is_valid_matrix(matrix):
    # create hashmap of position of all cells in the matrix
    complete_dic = create_hasmap(matrix)

    # check if the matrix is valid or not
    for dic in complete_dic:
        for element in complete_dic[dic]:
            frequency = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            for cell in complete_dic[dic][element]:
                if cell == 0:
                    continue
                frequency[cell] += 1
                if frequency[cell] > 1:
                    return False
    return True


# function that checks if the cell is still empty
# returns true if the cell is empty
def is_empty(cell):
    if cell == 0:
        return True
    else:
        return False


# function to check if there is an empty cell in the matrix
# if there is an empty cell, save the coordinates in the position variable
def find_empty_cell(matrix):
    global position
    position = [0, 0]
    for row in range(9):
        for cell in range(9):
            if matrix[row][cell] == 0:
                position[0] = row
                position[1] = cell
                return True
    return False


# recursive function
def solve_sudoku(matrix):
    # if there is no empty cell left, the sudoko is solved
    if not find_empty_cell(matrix):
        return True

    # extract the row and column nr from the position variable,
    # created in the find_empty_cell function
    row = position[0]
    col = position[1]

    # iterate over nrs 1 to 9
    for num in range(1, 10):

        # check if the matrix is safe
        if is_valid_matrix(matrix):
            matrix[row][col] = num

            # run the recursive function again if the sudoku is valid with the number
            if solve_sudoku(matrix):
                return True

            # if the number is not valid, set the cell again to 0
            matrix[row][col] = 0

    # trigger backtracking
    return False


# create main function
if __name__ == "__main__":

    # sudoku_matrix = [
    #     [3, 0, 6, 5, 0, 8, 4, 0, 0],
    #     [5, 2, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 8, 7, 0, 0, 0, 0, 3, 1],
    #     [0, 0, 3, 0, 1, 0, 0, 8, 0],
    #     [9, 0, 0, 8, 6, 3, 0, 0, 5],
    #     [0, 5, 0, 0, 9, 0, 6, 0, 0],
    #     [1, 3, 0, 0, 0, 0, 2, 5, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 7, 4],
    #     [0, 0, 5, 2, 0, 6, 3, 0, 0],
    # ]

    # if solve_sudoku(sudoku_matrix):
    #     print_matrix(sudoku_matrix)
    # else:
    #     print("no solution available")

    # output:
    # 5 2 9 1 3 4 7 6 8
    # 4 8 7 6 2 9 5 3 1
    # 2 6 3 4 1 5 9 8 7
    # 9 7 4 8 6 3 1 2 5
    # 8 5 1 7 9 2 6 4 3
    # 1 3 8 9 4 7 2 5 6
    # 6 9 2 3 5 1 8 7 4
    # 7 4 5 2 8 6 3 1 1

    # check if the solution is a valid one to check if the algorithm works
    test_matrix = [
        [3, 1, 6, 5, 7, 8, 4, 9, 2],
        [5, 2, 9, 1, 3, 4, 7, 6, 8],
        [4, 8, 7, 6, 2, 9, 5, 3, 1],
        [2, 6, 3, 4, 1, 5, 9, 8, 7],
        [9, 7, 4, 8, 6, 3, 1, 2, 5],
        [8, 5, 1, 7, 9, 2, 6, 4, 3],
        [1, 3, 8, 9, 4, 7, 2, 5, 6],
        [6, 9, 2, 3, 5, 1, 8, 7, 4],
        [7, 4, 5, 2, 8, 6, 3, 1, 1],
    ]
    print(is_valid_matrix(test_matrix))
