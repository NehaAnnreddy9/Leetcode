class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hm = defaultdict(list)
        for v,u in prerequisites: hm[u].append(v) 
        visited, rcs = set(), []
        
        def dfs(u):
            visited.add(u)
            rcs.append(u)
            
            for v in hm[u]:
                if v not in visited: 
                    if not dfs(v): return False
                elif v in rcs: return False
                
            rcs.pop()
            return True
        
        li = [u for u in hm] 
        for u in li:
            if u not in visited:
                if not dfs(u): return False
                
        return True
        
        
        
            
        