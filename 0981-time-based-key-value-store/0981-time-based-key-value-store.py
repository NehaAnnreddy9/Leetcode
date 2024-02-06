class TimeMap:

    def __init__(self):
        self.dt = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dt:
            self.dt[key].append((timestamp, value))
        else: self.dt[key] = [(timestamp, value)]
            
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.dt:
            bsv = self.dt[key]
            l, r = 0, len(bsv) - 1
            while l <= r:
                m = (l + r) // 2
                if bsv[m][0] <= timestamp:
                    res = bsv[m][1]
                    l = m + 1
                else: r = m - 1
                    
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)