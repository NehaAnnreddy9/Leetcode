import collections
class Solution(object):
    def pacificAtlantic(self, heights):
        po, ao = set(), set()
        m, n = len(heights), len(heights[0])
        
        def dfs(r,c,visited,prevH):
            if r < 0 or c < 0 or r == m or c == n or (r,c) in visited or heights[r][c] < prevH: return 
            visited.add((r,c))
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
            dfs(r+1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
             
        for c in range(n):
            dfs(0,c,po,heights[0][c])
            dfs(m-1,c,ao,heights[m-1][c])
            
        for r in range(m):
            dfs(r,0,po,heights[r][0])
            dfs(r,n-1,ao,heights[r][n-1])
                    
        return po & ao
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        