class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        longest = 0
        for n in nums: 
            if (n-1) not in ns:
                leng = 0
                while (n+leng) in ns: leng += 1
                longest = max(leng, longest)
        return longest
                
        
        