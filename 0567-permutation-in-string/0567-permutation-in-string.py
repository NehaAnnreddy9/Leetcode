class Solution(object):
    def checkInclusion(self, s1, s2):
        st = 0
        hm = defaultdict(int)
        hm1 = defaultdict(int)
        ws = len(s1)
        
        for i in s1: hm[i] += 1
        
        for e in range(len(s2)):
            hm1[s2[e]] += 1
            
            if e - st + 1 > ws:
                hm1[s2[st]] -= 1
                if hm1[s2[st]] == 0: del hm1[s2[st]]
                st += 1
                
            if hm == hm1: return True
            
        return False
                
            
            
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        