from collections import OrderedDict
class LRUCache(object):
    
    def __init__(self, capacity):
        self.od = OrderedDict()
        self.capacity = capacity
        
    def get(self, key):
        if key not in self.od: return -1
        self.od[key] = self.od.pop(key)
        return self.od[key]
        
    def put(self, key, value):
        if key in self.od: self.od.pop(key)
        elif self.capacity == len(self.od):
            self.od.popitem(last=False)
        self.od[key] = value
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)