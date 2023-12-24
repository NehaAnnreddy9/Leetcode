class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target: break
            elif s > target: r -= 1
            else: l += 1
            
        return [l+1, r+1]
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        