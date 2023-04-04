class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        k = 0
        for i in range(1,n):
            if nums[i] != nums[k]:
                if k != i-1:
                    nums[i],nums[k+1] = nums[k+1], nums[i]
                    k = k + 1
                else:
                     k = i
        return k + 1
