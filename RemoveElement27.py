class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        n = len(nums)
        p = n - 1
        if n == 0: return 0
        for i in range(n):
            if i == p: 
                if i == 0 and nums[0] != val: return 1
                if nums[p] != val: k = k + 1
                break
            if nums[i] == val:
                for j in range(p,i,-1):
                    p = j
                    if nums[j] != val:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                if j == 1 and nums[i] == val: return 0
            if nums[i] != val: k = k + 1
        return k



















      
