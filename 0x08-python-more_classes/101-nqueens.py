#!/usr/bin/python3


import sys

class NQueenSolver:
    """
    This class implements the N-Queens problem using backtracking.

    The N-Queens problem is a classic problem in computer science,
    where we are given a chessboard of size NxN, and we need to place
    N queens on it such that no two queens are in the same row, column,
    or diagonal.

    The class contains a board attribute, which is a 2D list of size NxN,
    where each element represents the presence of a queen in that cell.
    It also contains a solution attribute, which is a list of all possible
    solutions to the N-Queens problem.

    The solve method attempts to find a solution by placing queens in
    each row, starting from the first row. If a solution is found, it is
    added to the solution attribute. The isSafe method checks if a given
    row and column combination is safe for placing a queen. The isDiagonalSafe
    method checks if a given row and column combination is safe for placing
    a queen, by checking if there is a queen in any of the four diagonals.

    The printSolution method prints the current solution to the console.

    The validate_input method checks if the input provided by the user is
    valid, and if not, it prints an error message and exits the program.

    Attributes:
        board (list): A 2D list of size NxN, where each element represents
            the presence of a queen in that cell.
        solution (list): A list of all possible solutions to the N-Queens
            problem.
    """

    def __init__(self, n):
        """
        Initializes the class by setting the board and solution attributes
        to empty lists.

        Args:
            n (int): The size of the chessboard, i.e., the number of rows and
                columns.
        """

        self.n = n 
        self.board = [[0 for i in range(n)] for j in range(n)] # 2D list with n rows and n columns with each element initialized to 0
        self.solution = []

    def solve(self):
        """
        Attempts to find a solution to the N-Queens problem by placing queens
        in each row, starting from the first row. If a solution is found, it
        is added to the solution attribute.
        """

        if self.n == 0:
            self.solution.append(self.board)
            return

        for i in range(self.n):
            if self.isSafe(i):
                self.board[i][0] = 1
                self.solve()
                self.board[i][0] = 0
        return

    def isSafe(self, row):
        """
        Checks if a given row and column combination is safe for placing a queen.

        Args:
            row (int): The row index.
            col (int): The column index.

        Returns:
            bool: True if the row and column combination is safe, False otherwise.
        """

        for col in range(self.n):
            if self.board[row][col] == 1:
                return False
        for i in range(self.n):
            if self.isDiagonalSafe(row, i):
                return True
        return False

    def isDiagonalSafe(self, row, col):
        """
        Checks if a given row and column combination is safe for placing a queen,
        by checking if there is a queen in any of the four diagonals.

        Args:
            row (int): The row index.
            col (int): The column index.

        Returns:
            bool: True if the row and column combination is safe, False otherwise.
        """

        for i in range(row, self.n):
            if self.board[i][col] == 1:
                return False
        for i in range(col, self.n):
            if self.board[row][i] == 1:
                return False
        return True

    def printSolution(self):
        """
        Prints the current solution to the console.
        """

        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()
        return

    def validate_input():
        """
        Checks if the input provided by the user is valid, and if not, it
        prints an error message and exits the program.
        """

        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)

        try:
            N = int(sys.argv[1])
        except ValueError:
            print("N must be a number")
            sys.exit(1)

        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        return N
