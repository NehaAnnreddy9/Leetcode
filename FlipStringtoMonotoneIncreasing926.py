class Solution(object):
    def minFlipsMonoIncr(self, s):
        sl = len(s)
        c1 = 0
        res = 0
        for i in range(sl):
            if s[i] == "1": c1 += 1
            else:
                if c1 > 0: res = min(c1,res + 1)       
        return res
