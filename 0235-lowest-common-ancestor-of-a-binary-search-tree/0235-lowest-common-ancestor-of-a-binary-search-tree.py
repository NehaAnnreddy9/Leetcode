# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lca(self,root,p,q):
        if root == None: return
        if max(p.val,q.val) < root.val:
            return self.lca(root.left,p,q)
        elif min(p.val,q.val) > root.val:
            return self.lca(root.right,p,q)
        else: 
            return root
            
    def lowestCommonAncestor(self, root, p, q):
        return self.lca(root,p,q)
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        