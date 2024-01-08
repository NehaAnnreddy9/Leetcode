class Solution:
    def rob_ite(self, nums: List[int]) -> int:
        tmp1 = 0
        tmp2 = 0
        for cur in nums:
            tmp3 = tmp1
            tmp1 = max(cur + tmp2, tmp1)
            tmp2 = tmp3
        return tmp1
            
    def rob(self, nums: List[int]) -> int:
        if len(nums) > 1: return max(self.rob_ite(nums[1:]), self.rob_ite(nums[:-1]))
        return nums[0]
        