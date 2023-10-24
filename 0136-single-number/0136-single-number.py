class Solution(object):
    def singleNumber(self, nums):
        ln = len(nums)
        res = nums[0]
        for i in range(1,ln):
            res = res ^ nums[i]
        return res
        """
        :type nums: List[int]
        :rtype: int
        """
        