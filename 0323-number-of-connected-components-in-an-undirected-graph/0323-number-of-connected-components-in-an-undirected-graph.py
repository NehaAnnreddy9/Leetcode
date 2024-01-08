class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0] * n
        
        def find(x):
            if parent[x] != x: parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            xr, yr = find(x), find(y)
            if rank[xr] > rank[yr]: parent[yr] = xr
            elif rank[yr] > rank[xr]: parent[xr] = yr
            else:
                parent[yr] = xr
                rank[xr] += 1
            
        for u, v in edges: union(u, v)
            
        expars, fc = set(), 0 
        for p in parent:
            p = find(p)
            if p not in expars: 
                fc += 1
                expars.add(p)
        return fc
            
            