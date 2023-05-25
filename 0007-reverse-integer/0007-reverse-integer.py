class Solution(object):
    def reverse(self, x):
        num = abs(x)
        s = 0
        i = 0
        while num != 0:
            tar = num % 10
            num = num // 10
            s = (s * 10) + tar
            i += 1
        if s > (pow(2,31) - 1) or s < -pow(2,31): return 0
        return s if x > -1 else -s
            
        """
        :type x: int
        :rtype: int
        """
        