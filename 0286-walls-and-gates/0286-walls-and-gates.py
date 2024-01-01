import math, collections
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        m, n = len(rooms), len(rooms[0])
        q = collections.deque()
        visited = set()
        dirs = [[-1,0],[0,-1],[1,0],[0,1]]

        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    visited.add((r,c))
                    q.append([r,c])
        
    
        while q:
            for i in range(len(q)):
                r, c  = q.popleft()
                for dr, dc in dirs:
                    rw, cl = r + dr, c + dc
                    if rw < 0 or cl < 0 or rw == m or cl == n or (rw,cl) in visited:
                        continue
                    if rooms[rw][cl] == 2147483647:
                        rooms[rw][cl] = rooms[r][c] + 1
                        q.append([rw,cl])
                        visited.add((rw,cl))
                        
        return rooms
                
        """
        Do not return anything, modify rooms in-place instead.
        """
        