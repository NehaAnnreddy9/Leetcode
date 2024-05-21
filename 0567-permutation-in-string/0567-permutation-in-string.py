class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        l, r = 0, len(s1) - 1
        hp1, hp2 = defaultdict(int), defaultdict(int)
        
        for i in range(len(s1)):
            hp1[s1[i]] += 1
            hp2[s2[i]] += 1
        
        while r < len(s2):
            if hp1 == hp2: return True
            if hp2[s2[l]] == 1: del hp2[s2[l]]
            else: hp2[s2[l]] -=1 
            r += 1
            l += 1
            if r <= len(s2) - 1: hp2[s2[r]] += 1 
            
        if hp1 == hp2: return True
        return False
            
            
        