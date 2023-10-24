class Solution(object):
    def maxProfit(self, prices):
        lp = len(prices)
        i = 0
        j = 1
        prof = 0
        while i < lp and j < lp:
            if prices[i] >= prices[j]: 
                i = j
            else:
                val = prices[j] - prices[i]
                if val > prof: prof = val
            j += 1
        return prof
                
        
        """
        :type prices: List[int]
        :rtype: int
        """
        