class Solution(object):
    def postorderTraversal(self, root):
        if root == None: return None
        lis = []
        d = collections.deque()
        d1 = collections.deque()
        d.append(root)
        while len(d):
            p = d.pop()
            d1.append(p)
            if p.left: d.append(p.left)
            if p.right: d.append(p.right)
        while len(d1):
            lis.append(d1.pop().val)
        return lis
