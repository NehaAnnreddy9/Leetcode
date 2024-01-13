import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        msf, mnsf, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            tmp = max(nums[i], nums[i] * msf, nums[i] * mnsf)
            mnsf = min(nums[i], nums[i] * msf, nums[i] * mnsf)
            msf = tmp
            res = max(msf, res)
        return res
                
            
            
        