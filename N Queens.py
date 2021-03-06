'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
'''

class Solution:
    def totalNQueens(self, N: int) -> int:
        self.result = 0

        #Function to place a Queen while passing pass the board state (vert, ldiag, rdiag) as parameters
        def place(i: int, vert: int, ldiag: int, rdiag:int) -> None:
            # if end of board is being reached, increment counter of result
            if i == N: self.result += 1
            else:
                for j in range(N):
                    vmask, lmask, rmask = 1 << j, 1 << (i+j), 1 << (N-i-1+j)
                    if vert & vmask or ldiag & lmask or rdiag & rmask: continue
                    place(i+1, vert | vmask, ldiag | lmask, rdiag | rmask)

        place(0,0,0,0)
        return self.result