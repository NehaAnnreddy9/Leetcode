class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stk = []
        
        def func(oc, cc):
            if oc == n and cc == n:
                res.append("".join(stk))
                return
           
            if oc < n:
                stk.append('(')
                func(oc + 1, cc)
                stk.pop()
            
            if cc < n and cc < oc:
                stk.append(')')
                func(oc, cc + 1)
                stk.pop()
                
        func(0, 0)
        return res
        
            
        