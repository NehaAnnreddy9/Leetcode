class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        prefix_sums = [[0] * len(w) for w in wall]
        hmp = defaultdict(int)
        largest = 0
        for i, w in enumerate(wall):
            for j, num in enumerate(w):
                if 0 < j < len(w):
                    ps = sum(w[:j])
                    prefix_sums[i][j] = ps
                    hmp[ps] += 1
                    if hmp[ps] > largest: largest = hmp[ps]
    
                
        return len(wall) - largest
        
                
            
        
        