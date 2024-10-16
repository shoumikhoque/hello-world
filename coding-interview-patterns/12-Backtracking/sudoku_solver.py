import time


def solve_sudoku(board):
    def number_exists_in_row(number, r):
        return any(board[r][i] == number for i in range(9))

    def number_exists_in_col(number, c):
        return any(board[i][c] == number for i in range(9))

    def number_exists_in_sub_box(number, r, c):
        # Find the starting point of the 3x3 sub-box
        start_row = r - (r % 3)
        start_col = c - (c % 3)
        # Check all cells in the 3x3 sub-box
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == number:
                    return True
        return False

    def is_number_valid_for_placing(number, r, c):
        return (not number_exists_in_row(number, r) and
                not number_exists_in_col(number, c) and
                not number_exists_in_sub_box(number, r, c))

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for num in map(str, range(1, 10)):
                        if is_number_valid_for_placing(num, r, c):
                            # Place the number
                            board[r][c] = num
                            # Recursively solve the rest
                            if backtrack():
                                return True
                            # Backtrack: remove the number if it doesn't work
                            board[r][c] = '.'
                    return False  # No valid number found, trigger backtracking
        return True  # Solved

    # Start backtracking from the first cell
    backtrack()
    return board


def solve_sudoku_optimized(board):
    rows, cols = 9, 9

    # Initialize sets to track which numbers are used in each row, column, and sub-box
    rows_used = [set() for _ in range(9)]
    cols_used = [set() for _ in range(9)]
    sub_boxes_used = [set() for _ in range(9)]

    empty_cells = []

    # Fill the sets and find empty cells
    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                empty_cells.append((r, c))
            else:
                num = board[r][c]
                rows_used[r].add(num)
                cols_used[c].add(num)
                sub_boxes_used[(r // 3) * 3 + (c // 3)].add(num)

    def is_number_valid_for_placing(number, r, c):
        box_index = (r // 3) * 3 + (c // 3)
        return (number not in rows_used[r] and
                number not in cols_used[c] and
                number not in sub_boxes_used[box_index])

    def place_number(number, r, c):
        board[r][c] = number
        rows_used[r].add(number)
        cols_used[c].add(number)
        sub_boxes_used[(r // 3) * 3 + (c // 3)].add(number)

    def remove_number(number, r, c):
        board[r][c] = '.'
        rows_used[r].remove(number)
        cols_used[c].remove(number)
        sub_boxes_used[(r // 3) * 3 + (c // 3)].remove(number)

    def backtrack(index=0):
        # If we've placed numbers in all empty cells, the board is solved
        if index == len(empty_cells):
            return True

        r, c = empty_cells[index]

        for num in map(str, range(1, 10)):
            if is_number_valid_for_placing(num, r, c):
                # Place the number
                place_number(num, r, c)

                # Recur to place the next number
                if backtrack(index + 1):
                    return True

                # If placing the number didn't work, remove it (backtrack)
                remove_number(num, r, c)

        return False  # If no number is valid, trigger backtracking

    # Start backtracking from the first empty cell
    backtrack()

    return board


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    start_time=time.time()
    print(solve_sudoku(board))
    unoptimized=time.time()-start_time
    print('solved in : ' +str(unoptimized))
    start_time = time.time()
    print(solve_sudoku_optimized(board))
    optimized = time.time() - start_time
    print('solved in : ' + str(optimized))
    print('improved '+str(unoptimized/optimized)+' times')
