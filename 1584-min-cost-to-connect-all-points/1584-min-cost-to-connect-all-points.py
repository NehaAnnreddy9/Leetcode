import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visit, mc, ld = set(), 0, []
        for i in range(len(points)):
            ld.append({})
            for j in range(len(points)):
                if i != j: ld[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        minHp = [[ld[0][n],0,n] for n in ld[0]]
        heapq.heapify(minHp)
        visit.add(0)
    
        while len(visit) < len(points):
            mct, _, ni = heapq.heappop(minHp)
            if ni in visit: continue
            mc += mct
            visit.add(ni)
            for n in ld[ni]:
                if n not in visit: heapq.heappush(minHp, [ld[ni][n], ni, n])
                    
        return mc
            
        
        