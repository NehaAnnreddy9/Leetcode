class Solution(object):
    def containsDuplicate(self, nums):
        dict = {}
        ln = len(nums)
        for i in range(0,ln):
            if nums[i] in dict: return True
            dict[nums[i]] = i
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        