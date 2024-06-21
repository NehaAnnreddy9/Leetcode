# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        if root is None: return res
        q.append(root)
        
        while q:
            ql = len(q)
            li = []
            for i in range(ql):
                node = q.popleft()
                if node is not None:
                    q.append(node.left)
                    q.append(node.right)
                    li.append(node.val)
            if len(li): res.append(li)
            
        return res
            
        