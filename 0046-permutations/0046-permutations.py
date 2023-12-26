class Solution(object):
    def pd(self, nums, tmp, ans):
        if len(nums) == 0:
            ans.append(tmp[:])
            return
        
        for i in range(len(nums)):
            tmp.append(nums[i])
            self.pd(nums[:i]+nums[i+1:], tmp, ans)
            tmp.pop()
            
            
    def permute(self, nums):
        tmp = []
        ans = []
        self.pd(nums, tmp, ans)
        return ans
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        