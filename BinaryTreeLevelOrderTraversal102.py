class Solution(object):
    def levelOrder(self, root):
        if root == None: return None
        q = collections.deque()
        q.append(root)
        lis = []
        while len(q):
            cnt = len(q)
            ls = []
            for i in range(cnt):
                curr = q.popleft()
                ls.append(curr.val)
                if curr.left != None: q.append(curr.left)
                if curr.right != None: q.append(curr.right)
            lis.append(ls)
        return lis
