class Solution(object):
    pkey = 0
    def buildTree(self, preorder, inorder):
        return self.cbt(preorder,inorder,0,len(inorder)-1)
    
    def cbt(self, preorder, inorder, l, h):
        node = TreeNode(preorder[self.pkey])
        x = inorder.index(preorder[self.pkey])
        self.pkey = self.pkey + 1
        if l == h: return node
        if x != l: node.left = self.cbt(preorder, inorder,l,x-1)
        if x != h: node.right = self.cbt(preorder, inorder,x+1,h)
        return node
