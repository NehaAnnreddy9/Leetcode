import collections
class Solution(object):
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        cnt, rem_fresh = 0, 0
        q = collections.deque()
        dirs = [[-1,0],[0,-1],[1,0],[0,1]]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: rem_fresh += 1
                if grid[i][j] == 2: q.append([i,j])
                    
            
        while q and rem_fresh > 0: 
            for i in range(len(q)):
                rw, cl = q.popleft()  
                for dr, cr in dirs:
                    r, c = rw + dr, cl + cr
                    if -1 < r < m and -1 < c < n and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append([r,c])
                        rem_fresh -= 1
            cnt += 1
                            
        return cnt if rem_fresh == 0 else -1
                
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        