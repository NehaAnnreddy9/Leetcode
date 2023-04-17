class Solution(object):
    def binaryToDecimal(self,num):
        decimal, i = 0, 0
        while num != 0:
            dec = num % 10
            decimal = decimal + (dec * pow(2,i))
            num = num // 10
            i+=1
        return decimal

    def addBinary(self, a, b):
        a = self.binaryToDecimal(int(a))
        b = self.binaryToDecimal(int(b))
        res = str(bin(a + b))[2:]
        return res
