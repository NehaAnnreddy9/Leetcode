class Solution(object):
    def validPos(self,board,i,j,n,num):
        for l in range(n):
            if j!=l and i!=l and (board[i][l] == num or board[l][j] == num): return False
        s = int(math.sqrt(n))
        rs = i - (i % s)
        cs = j - (j % s)
        for m in range(s):
            for n in range(s):
                if i!=m+rs and j!=n+rs and board[m+rs][n+cs] == num: return False
        return True

    def isValidSudoku(self, board):
        n = len(board)
        for i in range(n):    
            for j in range(n):
                if board[i][j] != ".":
                    num = board[i][j]
                    if self.validPos(board,i,j,n,num) == False: return False
        return True
