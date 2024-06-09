class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [-1, -1]
        ci = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: 
                ci = m
                if nums[m] <= nums[r]:
                    l = m + 1
            elif nums[m] > target:
                r = m - 1
            else: l = m + 1
                
        res[1], l, r, ci = ci, 0, len(nums) - 1, -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: 
                ci = m
                if nums[m] >= nums[l]:
                    r = m - 1
            elif nums[m] > target:
                r = m - 1
            else: l = m + 1
                
        res[0] = ci
        return res
        