class Solution:
    def numDecodings(self, s: str) -> int:
        pt1, pt2 = 1, 1

        for i in range(len(s)-1, -1, -1):
            tmp = pt1
            if s[i] =="0": pt1 = 0
            else:
                if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")): pt1 += pt2
            pt2 = tmp
                
        return pt1
                