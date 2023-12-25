class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:     
        l = 1
        r = max(piles)
        res = r
        
        while l < r:
            mid = (l + r) // 2            
            hour_spent = 0
            
            for p in piles: hour_spent += math.ceil(p / mid)
            if hour_spent <= h: r = mid
            else: l = mid + 1
           
        return r
        
        