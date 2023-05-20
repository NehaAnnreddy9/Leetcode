class Solution(object):
    def canJump(self, nums):
        nl = len(nums)
        res = True
        lt = nl - 1
        for i in range(nl-2, -1, -1):
            if res == True:
                if nums[i] < 1: res = False
                else: lt = i
            else:
                if lt - i <= nums[i]: 
                    res = True
                    lt = i
        return res
            
        """
        :type nums: List[int]
        :rtype: bool
        """
        