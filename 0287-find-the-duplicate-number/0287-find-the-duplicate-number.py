class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f, s = 0, 0
        
        while True:
            f = nums[nums[f]] #4, 1, 3, 2, 4
            s = nums[s] #3, 4, 2, 3, 4
            if f == s: 
                s = 0
                while f != s:
                    f, s = nums[f], nums[s]
                return f
        