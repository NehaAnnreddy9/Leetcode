class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[-1,0],[0,-1],[1,0],[0,1]]
        m, n = len(board), len(board[0])
        rcs, wl = set(), len(word)
        
        def dfs(r, c, pos):
            if pos == wl: return True
            rcs.add((r, c))
            for rd, cd in dirs:
                rw, cl = r + rd, c + cd
                if -1 < rw < m and -1 < cl < n and (rw, cl) not in rcs and board[rw][cl] == word[pos]: 
                        if dfs(rw, cl, pos+1) == True:
                            rcs.remove((r, c))
                            return True
            rcs.remove((r, c))
            return False
            
            
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 1): return True
        
        return False
                    