import heapq, collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        q = collections.deque()
        time = 0
        
        while maxHeap or q:
            time += 1
            
            if len(maxHeap):
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt: q.append((cnt, time + n))
                    
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
                    
        return time   
            
            
            
        
        
        
        
        
        
        
        