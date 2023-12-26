class Solution(object):
    
    def csdfs(self, candidates, target, i, tmp, ans):
        if i == len(candidates): return
        if target == 0:
            ans.append(tmp[:])
            return
        elif target < 0: return
        
        #skip the current elem
        self.csdfs(candidates, target, i+1, tmp, ans)
        
        #include the current elem
        tmp.append(candidates[i])
        target = target - candidates[i]
        self.csdfs(candidates, target, i, tmp, ans)
        tmp.pop()
                
    def combinationSum(self, candidates, target):
        tmp = []
        ans = []
        self.csdfs(candidates, target, 0, tmp, ans)
        return ans
        
        
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        