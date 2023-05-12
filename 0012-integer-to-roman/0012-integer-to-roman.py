import numpy as np
from collections import OrderedDict
class Solution(object):
    def intToRoman(self, num):
        od = OrderedDict()
        od[1] = 'I'
        od[5] = 'V'
        od[10] = 'X'
        od[50] = 'L'
        od[100] = "C"
        od[500] = 'D'
        od[1000] = 'M'
        res = ''
        while num != 0:
            pick = 1
            if str(num)[0] == '4' or str(num)[0] == '9':
                for key in od:
                    if key > num: break
                n = num
                if num > 100: n = int(math.floor(num / 100.0)) * 100
                elif num > 10: n = int(math.floor(num / 10.0)) * 10
                pick = key - n
                res = res + od[pick] + od[key]
                num = num - key + pick
            else:
                sm = 5000
                for key in od:
                    if key == num:
                        pick = key
                        break
                    elif key < num and abs(key - num) < sm:
                        sm = abs(key - num)
                        pick = key    
                res = res + od[pick]
                num = num - pick
        return res
            
        """
        :type num: int
        :rtype: str
        """
        