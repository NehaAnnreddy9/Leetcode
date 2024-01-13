class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for i in range(amount+1)]
        dp[0] = 0
        
        for i in range(1, amount+1):
            m = 10001
            for coin in coins:
                if coin < i:
                    m = min(m, dp[coin] + dp[i-coin]) 
                elif coin == i: 
                    m = 1
                    break       
            dp[i] = m
            
        return dp[-1] if dp[-1] < 10001 else -1
        