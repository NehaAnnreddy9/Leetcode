class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        ans = [0] * n
        prod, lprod = 1, 1
        
        for i in range(n-1,-1,-1):
            prod = prod * nums[i]
            ans[i] = prod
            
        for i in range(n-1):
            ans[i] = lprod * ans[i+1]
            lprod = lprod * nums[i]
            
        ans[n-1] = lprod
        return ans
            
        
            