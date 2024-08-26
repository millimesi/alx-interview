#!/usr/bin/python3
""" The N queens puzzle """
import sys


def is_safe(board, row, col, N):
    """ Check if it's safe to place a queen at board[row][col] """
    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    """ Solve N Queens puzzle using backtracking """
    # base case: If all queens are placed, add solution to solutions
    if col >= N:
        solutions.append(board_to_positions(board, N))
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, N, solutions) or res
            board[i][col] = 0  # backtrack

    return res


def solve_nqueens(N):
    """ Solve N Queens puzzle and print the solution """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


def board_to_positions(board, N):
    """ Convert the board to a list of positions """
    positions = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                positions.append([i, j])
    return positions


def nqueens():
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)
    if N < 4:
        print('N must be at least 4')
        exit(1)

    solve_nqueens(N)


if __name__ == '__main__':
    nqueens()
