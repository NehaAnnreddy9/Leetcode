class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        le = len(edges)
        parent = [i for i in range(le+1)]
        rank = [0] * (le + 1)
        
        def find(x):
            if parent[x] != x: parent[x] = find(parent[x])
            return parent[x]
            
        def union(x, y):
            xr, yr = find(x), find(y)
            if xr == yr: return False
            if rank[xr] > rank[yr]: parent[yr] = xr
            elif rank[yr] > rank[xr]: parent[xr] = yr
            else: 
                parent[yr] = xr
                rank[xr] += 1
            return True
            
        
        for u, v in edges:
            if not union(u, v): return [u,v]