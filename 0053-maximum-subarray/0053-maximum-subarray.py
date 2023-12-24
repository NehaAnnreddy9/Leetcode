class Solution(object):
    def maxSubArray(self, nums):
        m = nums[0]
        s = nums[0]
        for i in range(1,len(nums)):
            if s < 0: s = nums[i]
            else: s = s + nums[i]
            m = max(s,m)
                
        return m
                
            
        """
        :type nums: List[int]
        :rtype: int
        """
        