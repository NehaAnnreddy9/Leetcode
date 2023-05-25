import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
    
        """
        nums = [-x for x in nums]
        heapq.heapify(nums)
        t = 0
        while k != 0:
            t = heapq.heappop(nums)
            k -= 1
        return -t
            
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        