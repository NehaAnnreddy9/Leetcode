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
                
                if curr.left != None and curr.right != None:
                    temp = curr.left
                    curr.left = curr.right
                    curr.right = temp
                    q.append(curr.left)
                    q.append(curr.right)
                    
    
                elif curr.right:
                    curr.left = curr.right
                    curr.right = None
                    q.append(curr.left)
                    
                    
                elif curr.left:
                    curr.right = curr.left
                    curr.left = None
                    q.append(curr.right)
                        
            return root
                
            
        
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        