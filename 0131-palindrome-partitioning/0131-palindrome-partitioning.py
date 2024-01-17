class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def dfs(i,tmp):
            nonlocal ans, s
            
            if i == len(s) - 1:
                if len(tmp) == 0:
                    if s == s[::-1]: ans.append([s])
                    return
                
                x, prev, fl = [], 0, 0
                for j in tmp:
                    st = s[prev:j+1] 
                    if st == st[::-1]:
                        x.append(st)
                        prev = j+1
                    else: 
                        fl = 1
                        break
                if fl == 0:
                    lt = s[prev:]
                    if lt == lt[::-1]:
                        x.append(lt)
                        ans.append(x) 
                return
            
            tmp.append(i)
            dfs(i+1,tmp)
            tmp.pop()
            
            dfs(i+1,tmp)
            
            
            
        dfs(0,[])        
        return ans
        