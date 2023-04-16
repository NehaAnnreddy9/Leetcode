class Solution(object):
    maxi = 0
    def minTm(self, root,target):
        if root == None: return -1
        l = self.minTm(root.left,target)
        r = self.minTm(root.right,target)
        if root.val == target:
            self.maxi = abs(min(l,r))
            return 0
        if l > -1: 
            self.maxi = max(self.maxi, 1+l+abs(r))
            return 1+l
        if r > -1: 
            self.maxi = max(self.maxi, 1+r+abs(l))
            return 1+r
        if l <= -1 and r <=-1: return min(l,r) - 1
        
    def amountOfTime(self, root, start):
        self.minTm(root,start)
        return self.maxi - 1
