class Solution(object):
    def strStr(self, haystack, needle):
        n = len(haystack)
        nl = len(needle)
        p = 0
        si = -1
        if nl > n: return -1
        i = 0
        while i < n:
            if p == nl: return i - nl
            if si != -1 and haystack[i] != needle[p]:
                p = 0
                i = si
                si = -1
            elif haystack[i] == needle[p]: 
                if p == 0: si = i
                p += 1 
            i += 1
        if p == nl: return i - nl
        return -1
