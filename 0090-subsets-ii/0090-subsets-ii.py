class Solution(object):
    
    def dfsdup(self, nums, ans, tmp, i):
        if i == len(nums): 
            ans.append(tmp[:])
            return
        
        
        
        #Include
        tmp.append(nums[i])
        self.dfsdup(nums, ans, tmp, i+1)
        tmp.pop()
        
        #Skip
        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        self.dfsdup(nums, ans, tmp, i+1)
        
        
        
    def subsetsWithDup(self, nums):
        ans = []
        tmp = []
        nums.sort()
        self.dfsdup(nums, ans, tmp, 0)
        return ans
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        