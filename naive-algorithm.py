recursion = 0

def check_soduku(row, column, number, matrix):
    check = 0
    for i in range(0, 9):
        if matrix[row][i] == number:
            check = 1
    for i in range(0, 9):
        if matrix[i][column] == number:
            check = 1
    row = row - row%3
    column =column - column%3

    for i in range(0, 3):
        for j in range(0, 3):
            if matrix[row+i][column+j] == number:
                check = 1

    if check == 1:
        return False
    else:
        return True

def sudoku_solver(matrix):
    recursion += 1
    break_condition = 0
    for i in range(0, 9):
        for j in range(0, 9):
            if matrix[i][j] == 0:
                break_condition = 1
                row = i
                column = j
                break
    
    if break_condition == 0:
        print("Naive Algorithm Sudoku Solution:")
        for i in matrix:
            print(i)
        print("Number of recursion:", recursion)
        exit(0)

    for i in range(0, 10):
        if check_soduku(row, column, i, matrix):
            matrix[row][column] = i
            if sudoku_solver(matrix):
                return True
            matrix[row][column] = 0

    return False

matrix = [
    [0,0,3,0,2,0,6,0,0],
    [9,0,0,3,0,5,0,0,1],
    [0,0,1,8,0,6,4,0,0],
    [0,0,8,1,0,2,9,0,0],
    [7,0,0,0,0,0,0,0,8],
    [0,0,6,7,0,8,2,0,0],
    [0,0,2,6,0,9,5,0,0],
    [8,0,0,2,0,3,0,0,9],
    [0,0,5,0,1,0,3,0,0]]

matrix2 = [
    [9, 0, 0, 0, 8, 0, 0, 0, 1],
    [0, 0, 0, 4, 0, 6, 0, 0, 0],
    [0, 0, 5, 0, 7, 0, 3, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 4, 0],
    [4, 0, 1, 0, 6, 0, 5, 0, 8],
    [0, 9, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 7, 0, 3, 0, 2, 0, 0],
    [0, 0, 0, 7, 0, 5, 0, 0, 0],
    [1, 0, 0, 0, 4, 0, 0, 0, 7]]

sudoku_solver(matrix2)