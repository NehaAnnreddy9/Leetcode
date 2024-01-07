class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans_stk, rcs, visited = [], [], set()
        hm, hmc = defaultdict(list), []
        
        for v, u in prerequisites: 
            hm[u].append(v)
            hmc.append(u)
        
        def dfs(u):
            visited.add(u)
            rcs.append(u)
        
            for v in hm[u]:
                if v not in visited: 
                    if not dfs(v): return False
                elif v in rcs: return False
        
            ans_stk.append(rcs.pop())
            return True
        
        for u in hmc:
            if u not in visited: 
                if not dfs(u): return []
                
        if len(ans_stk) != numCourses:
            for i in range(numCourses):
                if i not in visited: ans_stk.append(i)
                    
        return ans_stk[::-1]
            
            
            