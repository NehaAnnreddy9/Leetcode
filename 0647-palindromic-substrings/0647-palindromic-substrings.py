class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = set()
        lp, rp, n = 0, 0, len(s)
        
        def pss(l, r, pos):
            while l != -1 and r != n:
                if s[l] == s[r]: 
                    if (pos, s[l:r+1]) not in ans: ans.add((pos, s[l:r+1]))
                    l -= 1
                    r += 1
                else: break
        
        for i in range(n):
            pss(i, i, i)
            pss(i, i+1, i)
          
        return len(ans)
                
    
        