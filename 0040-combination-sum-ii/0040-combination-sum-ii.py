class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        li, res = [], []
        
        def dfs(i):
            s = sum(li)
            if s == target: 
                res.append(li.copy())
                return
            elif s > target or i == len(candidates): return
            
            li.append(candidates[i])
            dfs(i+1)
            li.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
                
            dfs(i+1)
        
        dfs(0)
        return res
            
            
        