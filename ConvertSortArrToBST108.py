class Solution(object):
    def sortedArrayToBST(self, nums):
        high = len(nums) - 1
        low = 0
        mid = int(math.ceil((low + high)/2))
        root = TreeNode(nums[mid])
        lis = [[mid,low,high,root]]
        while len(lis):
            el = lis.pop()
            low = el[1]
            high = el[0] - 1
            if low <= high: 
                mid = int(math.ceil((low + high)/2))
                el[3].left = TreeNode(nums[mid])
                lis.append([mid,low,high,el[3].left])
            low = el[0] + 1
            high = el[2] 
            if low <= high:  
                mid = int(math.ceil((low + high)/2))
                el[3].right = TreeNode(nums[mid])
                lis.append([mid,low,high,el[3].right])
        return root
