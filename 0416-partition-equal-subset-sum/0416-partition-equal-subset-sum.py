class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ts = sum(nums)
        if ts % 2 != 0 or len(nums) == 1: return False
        ssm = ts // 2 
        n = len(nums)
        dp = [[False for j in range(ssm+1)]for i in range(n+1)] 
        dp[0][0] = True
        for i in range(1,n+1):
            curr = nums[i-1]
            for j in range(ssm+1):
                if j < curr: dp[i][j] = dp[i-1][j]
                else: dp[i][j] = dp[i-1][j] or dp[i-1][j-curr]
                    
        return dp[n][ssm]
        
        