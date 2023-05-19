class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.v = []
        self.v.append(v1)
        self.v.append(v2)
        self.ptr1 = 0
        self.ptr2 = 0
        self.l1 = len(v1)
        self.l2 = len(v2)
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """

    def next(self):
        if self.hasNext():
            op = self.v[self.ptr1][self.ptr2]
            if self.ptr1 == 0: self.ptr1 = 1
            else:
                self.ptr1 = 0
                self.ptr2 += 1
            return op
        """
        :rtype: int
        """
        

    def hasNext(self):
        if self.ptr1 == 0:
            if self.ptr2 < self.l1: return True
            elif self.ptr2 < self.l2:
                self.ptr1 = 1
                return True
        if self.ptr1 == 1:
            if self.ptr2 < self.l2: return True
            elif self.ptr2 < self.l1 - 1:
                self.ptr1 = 0
                self.ptr2 += 1
                return True
        return False
        """
        :rtype: bool
        """
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())