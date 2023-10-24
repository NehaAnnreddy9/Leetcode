class Solution(object):
    def missingNumber(self, nums):
        ln = len(nums)
        return (((ln * (ln + 1)) / 2) - sum(nums))
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        