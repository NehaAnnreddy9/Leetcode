class Solution(object):
    def isSafe(self,row,col,sol,n):
        for i in range(row):
            if sol[i][col] == "Q":
                return False
        j = col
        for i in range(row,-1,-1):
            if sol[i][j] == "Q":
                return False
            j-=1
            if j == -1: break
        i = row
        for j in range(col,n+1):
            if sol[i][j] == "Q":
                return False
            i-=1
            if i == -1: break
        return True

    def NQueensRec(self,row,sol,n,final):
        if row == n+1: return True
        for i in range(n+1):
            if self.isSafe(row,i,sol,n):
                sol[row][i] = "Q"
                x = self.NQueensRec(row+1,sol,n,final)
                if x == True:
                    final.append([''.join(x) for x in sol])
                    return False
                elif x == False:
                    if row == n-1:
                        for i in range(n-1,n+1):
                            for j in range(n+1):
                                sol[i][j] = "."
                    else: 
                        return False
                sol[row][i] = "."

    def solveNQueens(self, n):
        sol= [["." for x in range(n)] for x in range(n)]
        final = []
        self.NQueensRec(0,sol,n-1,final)
        return final
