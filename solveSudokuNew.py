# https://leetcode.com/problems/sudoku-solver/solutions/3361836/love-babbar-solution/
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
    
        def isSafe(row, col, board, val):
            for i in range(9):
                if board[row][i] == str(val):
                    return False
                if board[i][col] == str(val):
                    return False
                
                # if board[row][i] == str(val) or board[i][col] == str(val):
                #     return False
                
                # KYU THIS ->
                if board[3*(row//3) + i//3][3*(col//3) + i%3] == str(val):
                    return False
            return True

        def solve(board):
            n = len(board[0])
            for row in range(n):
                for col in range(n):
                    if board[row][col] == '.':
                        for val in range(1, 10):
                            if isSafe(row, col, board, val):
                                board[row][col] = str(val)
                                nextPosibility = solve(board)
                                if nextPosibility:
                                    return True
                                else:
                                    board[row][col] = '.'
                        return False
            return True

        solve(board)
