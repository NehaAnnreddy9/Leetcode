import math
class Solution(object):
    def kClosest(self, points, k):
        hp = []
        ans = []
        for point in points:
            elem = (math.sqrt(point[0]**2 + point[1]**2),) + (point,)
            heapq.heappush(hp, elem)
            
        while k > 0:
            ans.append(heapq.heappop(hp)[1])
            k -= 1
        return ans
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        