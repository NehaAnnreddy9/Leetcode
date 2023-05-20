class Solution(object):
    res = 0
    def generateParenthesis(self, n):
        self.res = []
        self.generateParenthesisrec(n,1,0,'(')
        return self.res
    
    def generateParenthesisrec(self,n,op,cl,r):
        if op == n and cl < n:
            while cl < n:
                r = r + ')'
                cl += 1
            self.res.append(r)
            return
        elif op == cl and op < n:
            r = r + "("
            op += 1
            self.generateParenthesisrec(n,op,cl,r)
        elif op < n:
            self.generateParenthesisrec(n,op+1,cl,r + '(')
            self.generateParenthesisrec(n,op,cl+1,r + ')')
        
        """
        :type n: int
        :rtype: List[str]
        """
        