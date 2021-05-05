from collections import Counter

def read_sudokus(file_path):
    "Reads the sudokus from file."
    sudokus = []

    with open(file_path, "r") as sudoku_file:
        numbers = []
        for line in sudoku_file:
            
            if line.startswith("Grid"):
                if numbers:
                    sudokus.append(numbers)
                numbers = []

            else:
                line = line.strip("\n")
                for char in line:
                    numbers.append(int(char))

        if numbers:
            sudokus.append(numbers)

    return sudokus

def calculate_answer(sudokus):
    "Solves the sudokus and prints out the sum of the starting 3-digit numbers from the solutions."
    total = 0

    for sudoku in sudokus:
        zeroes = []

        for i in range(81):
            if sudoku[i] == 0:
                zeroes.append(i)

        sudoku = solve_sudoku(sudoku, zeroes)
        total += 100 * sudoku[0] + 10 * sudoku[1] + sudoku[2]

    print(total)

def solve_sudoku(sudoku, zeroes):
    "Solves the given sudoku."
    sudoku[zeroes[0]] = 1
    index = 0

    while 0 in sudoku:
        if check_valid(sudoku, zeroes[index]):
            index += 1
            sudoku[zeroes[index]] = 1

        else:
            sudoku, index = backtrack(sudoku, zeroes, index)

    return sudoku

def check_valid(sudoku, position):
    "Checks whether the new number fits in the given position or not."
    value = sudoku[position]

    row_num = position//9
    col_num = position%9

    row = sudoku[row_num * 9:(row_num + 1) * 9]
    if Counter(row)[value] != 1:
        return False

    column = [sudoku[i] for i in range(col_num, 81, 9)]
    if Counter(column)[value] != 1:
        return False

    box_row = row_num//3
    box_col = col_num//3

    box = [sudoku[9 * r + c] for r in range(3 * box_row, 3 * (box_row + 1)) for c in range(3 * box_col, 3 * (box_col + 1))]
    if Counter(box)[value] != 1:
        return False

    return True

def backtrack(sudoku, zeroes, index):
    "Moves to the next possibility after a failed attempt."
    while sudoku[zeroes[index]] == 9:
        sudoku[zeroes[index]] = 0
        index -= 1

    sudoku[zeroes[index]] += 1
    return sudoku, index

if __name__ == "__main__":
    sudokus = read_sudokus("Data/sudoku.txt")
    calculate_answer(sudokus)
