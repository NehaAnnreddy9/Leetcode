class Solution:
    def jump(self, nums: List[int]) -> int:
        ln = len(nums) 
        if ln == 1 or ln == 2: return ln - 1
        ml, i = 0, 0
        
        while i < ln - 1:
            mxv, mi = -1, -1
            for j in range(i, i + nums[i] + 1): 
                if j == ln - 1: return ml + 1
                if mxv < nums[j] + j: mxv, mi = nums[j] + j, j 
            i = mi
            ml += 1
                
        return ml
            
            
            
            
        