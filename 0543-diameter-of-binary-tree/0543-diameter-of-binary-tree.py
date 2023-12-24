# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dm = 0
        def dfslen(root):
            if root == None: return 0
            nonlocal dm
            l = dfslen(root.left)
            r = dfslen(root.right)
            dm = max(dm, l + r)
            return max(l,r) + 1
        
        dfslen(root)
        return dm
        