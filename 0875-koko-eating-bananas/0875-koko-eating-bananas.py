class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:     
        l = 1
        r = max(piles)
        
        while l < r:
            mid = (l + r) // 2            
            hour_spent = 0
            
            for p in piles: hour_spent += math.ceil(p / mid)
            if hour_spent <= h: r = mid #We keep doing this to get to the lowest val that satisfies h_s == h, r could be higher than lowest val but could satisfy the condn, so we keep coming to this condition till l == r, when the lowest possible value (l) satisfies our condn
            else: l = mid + 1 #We need to get the lowest value that satisfies h_s == h so we will eliminate all vals from l to mid inclusive that don't satisfy here
           
        return l
        
        