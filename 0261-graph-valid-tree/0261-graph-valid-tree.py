from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dt = defaultdict(list)
        component_number = 0
        for (u, v) in edges: 
            dt[u].append(v)
            dt[v].append(u)
        visited = [False] * n
            
        def dfs(v, parent):
            visited[v] = True
            for neighbor in dt[v]:
                if not visited[neighbor]:
                    if not dfs(neighbor, v):
                        return False
                elif neighbor != parent:
                    return False

            return True

        
        for vertex in range(n):
            if not visited[vertex]:
                component_number += 1
                if component_number > 1: return False  
                if not dfs(vertex, -1): return False  

        return True

        
        
           
                
                
            
        