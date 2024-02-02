# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cgn = 0
        stk = [(root, float('-inf'))]
        while stk:
            node, msf = stk.pop()
            if msf <= node.val: cgn += 1
            if node.left: stk.append((node.left, max(node.val, msf)))
            if node.right: stk.append((node.right, max(node.val, msf)))
            
        return cgn
            
                
        