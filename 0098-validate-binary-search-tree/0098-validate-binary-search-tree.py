# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    res = 0
    def isValidBST(self, root):
        self.res = []
        self.vlbst(root)
        lr = len(self.res)
        for i in range(1,lr):
            if self.res[i] <= self.res[i-1]: return False
        return True
            
    def vlbst(self,root):         
        if root == None: return
        self.vlbst(root.left)
        self.res.append(root.val)
        self.vlbst(root.right)
            
        """
        :type root: TreeNode
        :rtype: bool
        """
        