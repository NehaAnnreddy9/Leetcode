# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution(object):
    def flatten(self, root):
        st = collections.deque()
        p = root
        while len(st) > 0 or p != None:
            if p.left != None:
                if p.right != None: st.append(p.right)
                p.right = p.left
                p.left = None
            elif p.right == None and p.left == None:
                if len(st) > 0: p.right = st.pop()
                else: break
            p = p.right
        return root
        
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        