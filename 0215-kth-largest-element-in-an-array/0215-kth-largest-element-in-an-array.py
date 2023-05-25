import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
        
        """
        k = len(nums) - k
        heapq.heapify(nums)
        t = 0
        while k != -1:
            t = heapq.heappop(nums)
            k -= 1
        return t
        """