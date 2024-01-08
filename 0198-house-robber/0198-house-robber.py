class Solution:
    def rob(self, nums: List[int]) -> int:
        ln = len(nums)
        ans = [0] * ln
        ans[0] = nums[0]
        
        if ln > 1:
            ans[1] = max(nums[0], nums[1])
            
            for i in range(2, ln):
                ans[i] = max(ans[i-1], ans[i-2] + nums[i])
        
        return ans[-1]
        