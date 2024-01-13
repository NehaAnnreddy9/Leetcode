class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subarr = []
        
        for n in nums:
            ind = bisect_left(subarr, n)
            if ind == len(subarr): subarr.append(n)
            else: subarr[ind] = n
                
        return len(subarr)
        