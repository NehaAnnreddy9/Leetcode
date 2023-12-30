class Solution(object):
    def insert(self, intervals, newInterval):
        li = len(intervals)
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        ans = [intervals[0]]
            
        for j in range(li+1): 
            if intervals[j][0] <= ans[-1][1]:
                ans[-1][1] = max(intervals[j][1],ans[-1][1])
            else: ans.append(intervals[j])
 
            
        return ans
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        