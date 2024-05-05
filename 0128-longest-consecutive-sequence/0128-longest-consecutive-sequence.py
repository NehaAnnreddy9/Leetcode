class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        largest = 0
        hmp = set(nums)
        for n in nums:
            l = 1
            if n - 1 not in hmp:
                while n + 1 in hmp: 
                    l += 1
                    n += 1
            if l > largest: largest = l
        return largest
            
      
        
        