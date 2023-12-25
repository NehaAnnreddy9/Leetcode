class Solution(object):
    def characterReplacement(self, s, k):
        st = 0
        hm = {}
        mws = 0
        
        for e in range(0,len(s)):
            if s[e] in hm: hm[s[e]] += 1
            else: hm[s[e]] = 1
                
            if ((e - st + 1) - max(hm.values())) > k:
                hm[s[st]] -= 1
                st += 1
                
            mws = max(mws, e - st + 1)
                             
        return mws
            
        
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        