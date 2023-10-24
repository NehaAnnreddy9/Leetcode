class Solution(object):
    def isAnagram(self, s, t):
        dict = {}
        sl = len(s)
        tl = len(t)
        for i in range(0,sl):
            if s[i] in dict: dict[s[i]] += 1
            else: dict[s[i]] = 1
        for i in range(0,tl):
            if t[i] in dict: dict[t[i]] -= 1
            else: return False
        for val in dict.values():
            if val != 0: return False
        return True
            
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        