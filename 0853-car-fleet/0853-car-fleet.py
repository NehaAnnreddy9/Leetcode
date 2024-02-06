class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets, stk = [], []
        for i in range(len(position)): fleets.append((position[i], speed[i]))
        for (p, s) in sorted(fleets)[::-1]:
            stk.append((target - p) / s)
            if len(stk) >= 2 and stk[-1] <= stk[-2]: stk.pop()
        
        return len(stk)
        
        