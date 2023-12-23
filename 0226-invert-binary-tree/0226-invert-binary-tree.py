# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def invertTree(self, root):
        if root != None:
            q = deque([root])
            while q:
                curr = q.popleft()
                
                curr.left, curr.right = curr.right, curr.left
    
                if curr.right:
                    q.append(curr.right)
                    
                    
                if curr.left:
                    q.append(curr.left)
                        
            return root
                
            
        
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        