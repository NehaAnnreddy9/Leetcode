class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        k = 0
        
        def dfs(x, y):
            nonlocal k
            visited.add((x, y))
            ngb = [[-1, 0], [0,-1], [1, 0], [0, 1]]
            for r, c in ngb:
                nr, nc = x + r, y + c
                if (nr, nc) not in visited and -1 < nr < len(board) and -1 < nc < len(board[0]) and board[nr][nc] == word[k]:
                    k += 1
                    if k == len(word): return True
                    if dfs(nr, nc): return True
                    else: k -= 1
            visited.remove((x, y))
            return False
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    k = 1
                    if k == len(word): return True
                    if dfs(i, j): return True
                    else: visited.clear()
                    
        return False
                    