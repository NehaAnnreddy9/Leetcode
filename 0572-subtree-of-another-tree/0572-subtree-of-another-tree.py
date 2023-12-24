# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def is_identical(self, root, subRoot):
        if root == None or subRoot == None: 
            return root is None and subRoot is None
        
        if root.val == subRoot.val:
            if self.is_identical(root.left, subRoot.left) == True and self.is_identical(root.right, subRoot.right) == True:
                return True
        return False

    def isSubtreedfs(self, root, subRoot):
        if root == None or subRoot == None: 
            return root is None and subRoot is None
        
        if self.is_identical(root, subRoot): return True
            
        if self.isSubtreedfs(root.left, subRoot) == True or self.isSubtreedfs(root.right, subRoot) == True:
                return True
        
        return False
        
    def isSubtree(self, root, subRoot):
        return self.isSubtreedfs(root, subRoot)
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        