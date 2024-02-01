class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        st, tt = 0, 0
        for i in range(len(gas)):
            tt += gas[i] - cost[i]
            if tt < 0: 
                tt = 0
                st = i + 1                   
        return st
        