class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last, res = {}, []
        for i in range(len(s)): last[s[i]] = i
        size, ei = 0, 0
        for i, c in enumerate(s):
            size += 1 
            ei = max(ei, last[c])
            if i == ei: 
                res.append(size)
                size = 0
        return res
        