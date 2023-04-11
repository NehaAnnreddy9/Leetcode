class Solution(object):
    def inorderTraversal(self, root):
        if root == None: return None
        lis = []
        d = collections.deque()
        p = root
        d.append(root)
        while len(d) != 0:
            p = d[-1].left
            if p != None: d.append(p)
            else: 
                p = d.pop()
                lis.append(p.val)
                while True:
                    if p.right != None: 
                        d.append(p.right)
                        break
                    else: 
                        if len(d) == 0: break
                        p = d.pop()
                        lis.append(p.val)
        return lis
