class Solution(object):
    def merge(self, intervals):
        li = len(intervals)
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        ans = [intervals[0]]
   
        for i in range(1,li):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(intervals[i][1],ans[-1][1])
            else: ans.append(intervals[i])
 
            
        return ans
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        