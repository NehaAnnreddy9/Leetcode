class TimeMap:

    def __init__(self):
        self.tmp = defaultdict(list)
        
    def get_pos(self, key: str, timestamp: int) -> int:
        l, r = 0, len(self.tmp[key])  - 1
        while l <= r:
            m = (l+r) // 2
            if timestamp >= self.tmp[key][m][0]:
                l = m + 1
            else:
                r = m - 1
        return l
        
      
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmp[key].insert(self.get_pos(key, timestamp), (timestamp, value))
           
    def get(self, key: str, timestamp: int) -> str:
        if not len(self.tmp[key]): return ""
        l, r = 0, len(self.tmp[key])  - 1
        res = ""
        while l <= r:
            m = (l+r) // 2
            if timestamp >= self.tmp[key][m][0]:
                res = self.tmp[key][m][1]
                l = m + 1
            else:
                r = m - 1
        return res
                
            
            
       
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)