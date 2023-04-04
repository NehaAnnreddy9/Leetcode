class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1
        mid = 0
        if high == 0:
            if nums[0] < target: return 1
            return 0
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] < target: low = mid + 1
            elif nums[mid] > target: high = mid - 1
            elif nums[mid] == target: return mid
            if low > high: return low
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
