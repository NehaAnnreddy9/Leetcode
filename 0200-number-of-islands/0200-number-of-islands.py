import collections
class Solution(object):
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        cn = 0
        visit = set()
        
        def bfsisl(r, c):
            q = collections.deque([])
            q.append((r, c))
            dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        
            while q:
                row, col = q.popleft()
                for dr, cr in dirs:
                    r, c = row + dr, col + cr
                    if -1 < r < m and -1 < c < n and grid[r][c] == "1" and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))
                        
            
                        
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == '1' and (i,j) not in visit:
                    visit.add((i, j))
                    bfsisl(i, j)
                    cn += 1
                     
        return cn
        
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        