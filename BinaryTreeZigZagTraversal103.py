lass Solution(object):
    def zigzagLevelOrder(self, root):
        if root == None: return None
        q = collections.deque()
        q.append(root)
        stk = []
        lis = [] 
        while len(q):
            cnt = len(q)
            ls = []
            for i in range(cnt):
                curr = q.popleft()
                ls.append(curr.val)
                if curr.left != None: 
                    stk.append(curr.left)
                    if curr.left.left != None: q.append(curr.left.left)
                    if curr.left.right != None: q.append(curr.left.right)
                if curr.right != None: 
                    stk.append(curr.right)
                    if curr.right.left != None: q.append(curr.right.left)
                    if curr.right.right != None: q.append(curr.right.right)
            lis.append(ls)
            if len(stk):
                ls = []
                while len(stk): ls.append(stk.pop().val)
                lis.append(ls)
        return lis
