class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures)
        stk = []
        
        for i in range(len(temperatures)):
            while len(stk):
                if stk[-1][1] < temperatures[i]:
                    (j,tmp) = stk.pop()
                    ans[j] = i - j
                else: break
             
            stk.append((i,temperatures[i]))
            
        return ans
            
            
            
             
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        