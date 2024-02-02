class Solution:
    def myPow(self, x: float, n: int) -> float:
        def intPow(v, e):
            if e == 0: return 1
            if e % 2 == 0:  return intPow(v * v, e // 2)
            return v * intPow(v * v, (e - 1) // 2)
        
        if n < 0: 
            fin = intPow(x, -n)
            return (1/fin)
        return intPow(x, n)
        