import collections
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.v = [v1,v2]
        self.q = collections.deque()
        for i,vec in enumerate(self.v):
            if len(vec) > 0: self.q.append((i,0))
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """

    def next(self):
        if self.hasNext():
            i,veci = self.q.popleft()
            if veci + 1 < len(self.v[i]): self.q.append((i,veci+1))
            return self.v[i][veci]
        """
        :rtype: int
        """
        
    def hasNext(self):
        return len(self.q) > 0
        """
        :rtype: bool
        """
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())