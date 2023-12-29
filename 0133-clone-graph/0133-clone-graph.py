"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        hm = {}
        q = deque([node])
        hm[node] = Node(node.val,[])
        while q:
            nd = q.popleft()
            for neig in nd.neighbors:
                if neig not in hm:
                    hm[neig] = Node(neig.val, [])
                    q.append(neig)
                
                hm[nd].neighbors.append(hm[neig])
             
        return hm[node]
        