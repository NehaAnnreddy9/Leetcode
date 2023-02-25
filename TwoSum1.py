class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in range(0,len(nums)):
                compl = target - nums[i]
                if(compl in dict.values()):
                    x = list(dict.values()).index(compl)
                    y = i
                    return x,y
                dict[i] = nums[i]
        return []
