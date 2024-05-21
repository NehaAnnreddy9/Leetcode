class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        l, r = 0, 0
        hp1, hp2 = defaultdict(int), defaultdict(int)
        
        for i in range(len(s1)):
            hp1[s1[i]] += 1
        
        while r < len(s2):
            hp2[s2[r]] += 1 
            if hp1 == hp2: return True
            if (r-l+1) == len(s1):
                if hp2[s2[l]] == 1: del hp2[s2[l]]
                else: hp2[s2[l]] -=1 
                l += 1
            r += 1
        
        return False
            
            
        