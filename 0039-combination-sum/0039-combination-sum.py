class Solution(object):
    
    def csdfs(self, candidates, target, i, tmp, ans):
        if i == len(candidates): return
        s = sum(tmp)
        if s == target:
            ans.append(tmp[:])
            return
        elif s > target: return
        
        #skip the current elem
        self.csdfs(candidates, target, i+1, tmp, ans)
        
        #include the current elem
        tmp.append(candidates[i])
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
        