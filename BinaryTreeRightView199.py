class Solution(object):
    def rightSideView(self, root):
        if root == None: return None
        lis = []
        q = collections.deque()
        q.append(root)
        lis.append(root.val)
        q.append(None)
        curr = root
        while len(q) > 1:
            while curr != None:
                if curr.right != None: q.append(curr.right)
                if curr.left != None: q.append(curr.left)
                curr = q.popleft()
            q.append(None)
            curr = q.popleft()
            if curr != None: lis.append(curr.val)
        return lis
