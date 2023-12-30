import collections
class Solution(object):
    def maxAreaOfIsland(self, grid):
        m = len(grid)
        n = len(grid[0])
        visited = set()
        maxarea = 0
        
        def bfsmax(r, c):
            q = collections.deque([(r,c)])
            ma = 1
            dirs = [[0,-1],[0,1],[-1,0],[1,0]]
            
            while q:
                rw, cl = q.popleft()
                for dr, cr in dirs:
                    r, c = rw + dr, cl + cr
                    if -1 < r < m and -1 < c < n and grid[r][c] == 1 and (r,c) not in visited:
                        visited.add((r,c))
                        q.append((r,c))
                        ma += 1
            return ma

        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    visited.add((i,j))
                    maxarea = max(bfsmax(i,j), maxarea)
                            
        return maxarea
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        