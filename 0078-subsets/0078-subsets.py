class Solution(object):
    def subsets(self, nums):
        num = len(nums)
        res = []
        n = pow(2,num)
        for i in range(n):
            r = []
            for j in range(num):
                if i & pow(2,j) > 0: r.append(nums[j])
            res.append(r)
        return res
        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        