class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        visited = set()
        dirs = [[-1,0],[0,-1],[1,0],[0,1]]
        
        def dfs(r, c):
            if (r, c) not in visited:
                visited.add((r, c))
                for rd, cd in dirs:
                    rw, cl = r + rd, c + cd
                    if -1 < rw < m and -1 < cl < n: 
                        if board[rw][cl] == 'O': dfs(rw, cl)
                                      
        for i in range(m):
            if board[i][0] == 'O': dfs(i, 0)
            if board[i][n-1] == 'O': dfs(i, n-1)
            
        for j in range(n):
            if board[0][j] == 'O': dfs(0, j)
            if board[m-1][j] == 'O': dfs(m-1, j)
                
        
        for i in range(1,m-1):
            for j in range(1,n-1):
                if (i,j) not in visited and board[i][j] == "O": board[i][j] = "X"
                    
        return board
        """
        Do not return anything, modify board in-place instead.
        """
        