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
        return self.vlbst(root)
                 
    def vlbst(self,root):         
        if root == None: return True
        if self.vlbst(root.left) == False: return False
        lr = len(self.res)
        if lr > 0 and self.res[lr-1] >= root.val: return False
        self.res.append(root.val)
        if self.vlbst(root.right) == False: return False
        return True    
        """
        :type root: TreeNode
        :rtype: bool
        """
        