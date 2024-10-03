# This method determines if a queen can be placed at proposed_row, proposed_col
# with current solution i.e. this move is valid only if no queen in current
# solution may attack the square at proposed_row and proposed_col
def is_valid_move(proposed_row, proposed_col, solution):
    for i in range(0, proposed_row):
        old_row = i
        old_col = solution[i]
        diagonal_offset = proposed_row - old_row
        if (old_col == proposed_col or old_col == proposed_col - diagonal_offset or old_col == proposed_col + diagonal_offset):
            return False
    return True

# Recursive worker function
def solve_n_queens_rec(n, solution, row, results):
    if row == n:
        results.append(solution[:])
        return
    for i in range(0, n):
        if is_valid_move(row, i, solution):
            solution[row] = i
            solve_n_queens_rec(n, solution, row + 1, results)

# Function to solve N-Queens problem
def solve_n_queens(n):
    results = []
    solution = [-1] * n

    solve_n_queens_rec(n, solution, 0, results)

    return len(results)

if __name__ == '__main__':
    n = [14]
    for i in range(len(n)):
        print(i + 1, ".\t Queens: ",
              n[i], ", Chessboard: (", n[i], "x", n[i], ")", sep="")
        res = solve_n_queens(n[i])
        print("\n\t Total solutions count for ",
              n[i], " queens on a ", n[i], "x", n[i], " chessboard: ", res, sep="")
        print("-" * 100, "\n", sep="")