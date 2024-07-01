import heapq, collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mH = Counter(tasks)
        mH = [-1*num for num in mH.values()]
        heapq.heapify(mH)
        
        q = collections.deque()
        time = 0
        
        while mH or q:
            if mH: 
                f = heapq.heappop(mH)
                if f+1 < 0: q.append([f+1,time + n + 1])
            time = time + 1
            if q and q[0][1] == time:
                heapq.heappush(mH, q.popleft()[0])
                
        return time
            
                
        
            
            
            
        
        
        
        
        
        
        
        