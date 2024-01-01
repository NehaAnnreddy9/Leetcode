class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        tmp = []
        candidates.sort()
        
        def dfs(pos,target):
            if target == 0: ans.append(tmp[:])
            if target <= 0: return  
            prevC = -1
            
            for i in range(pos, len(candidates)):
                if candidates[i] == prevC: continue
                tmp.append(candidates[i])
                dfs(i+1,target - candidates[i])
                tmp.pop()                
                prevC = candidates[i]
                 
        dfs(0, target)
        return ans
            
            
        