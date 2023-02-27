class Solution(object):
    def isSafe(self,board,i,j,num,n):
        for l in range(n):
            if board[i][l] == num or board[l][j] == num: return False
        s = int(math.sqrt(n))
        rs = i - (i % s)
        cs = j - (j % s)
        for m in range(s):
            for n in range(s):
                if board[m+rs][n+cs] == num: return False
        return True

    def sudoku_solver_rec(self,board,n):
        for i in range(n):    
            for j in range(n):
                if board[i][j] == ".": break
            if board[i][j] == ".": break
        if i == n-1 and j == n-1 and board[i][j] != '.': return True
        for k in range(1,n+1):
            if self.isSafe(board,i,j,str(k),n) == True:
                board[i][j] = str(k)
                if self.sudoku_solver_rec(board,n) == True: return True
                board[i][j] = "."
        return False

    def solveSudoku(self, board):
        n = len(board)
        if self.sudoku_solver_rec(board,n) == True:
            return board
