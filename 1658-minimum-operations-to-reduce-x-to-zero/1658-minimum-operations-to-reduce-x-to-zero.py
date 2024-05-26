class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0: return -1
        elif target == 0: return len(nums)
        l, r = 0, 0
        count = 0
        ws = 0
        
        while r < len(nums):
            count += nums[r]
            
            while count > target and l <= r:
                count -= nums[l]
                l += 1
                
            if count == target: 
                ws = max(ws, r - l + 1)
                
            r += 1
            
        return len(nums) - ws if ws != 0 else -1
        
        
        
        