import math
class MinStack(object):

    def __init__(self):
        self.stk = []
        self.m_stk = []
        
    def push(self, val):
        self.stk.append(val)
        if len(self.m_stk) == 0 or val <= self.m_stk[-1]: self.m_stk.append(val)
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        val = self.stk.pop()
        if val == self.m_stk[-1]: self.m_stk.pop()
        """
        :rtype: None
        """
        

    def top(self):
        return self.stk[-1]
        """
        :rtype: int
        """
        

    def getMin(self):
        return self.m_stk[-1]        
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()