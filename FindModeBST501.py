class Solution(object):
    def findMode(self, root):
        q = {}
        q = self.fmrec(root,q)
        m = 0
        l = []
        for k in q: 
            if m < q[k]: m = q[k]
        for k in q: 
            if q[k] == m: l.append(k)
        return l

    def fmrec(self,r,q):
        if r == None: return q
        if r.val in q: q[r.val]+= 1
        else: q[r.val] = 1
        q = self.fmrec(r.left,q)
        q = self.fmrec(r.right,q)
        return q
