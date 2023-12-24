class Solution(object):
    def topKFrequent(self, nums, k):
        hm = {}
        for i in nums:
            if i in hm: hm[i] += 1
            else: hm[i] = 1
                
        ans = []      
        for i in hm: ans.append((-hm[i],i))   
        heapq.heapify(ans)
        
        a = []
        for i in range(k): a.append(heapq.heappop(ans)[1])
        return a
            
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        