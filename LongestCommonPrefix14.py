class Solution(object):
    def longestCommonPrefix(self, strs):
        n = len(strs[0])
        if len(strs) == 1: return strs[0]
        fst = strs[0]
        if n == 0: return ""
        for i in range(n):
            for stn in strs:
                ls = len(stn)
                if ls == 0: return ""
                if i == ls or stn[i] != fst[i]:
                    return stn[:i]
            if i == n-1: return fst
            
        """
        :type strs: List[str]
        :rtype: str
        """
