class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        min_cnt = 0
        i = 1
        prev_vals = [intervals[0][0], intervals[0][1]]
        while i < len(intervals):
            if prev_vals[1] > intervals[i][0]:
                min_cnt += 1
                if (prev_vals[1]  > intervals[i][1]):
                    prev_vals = [intervals[i][0], intervals[i][1]]
            else: prev_vals = [intervals[i][0], intervals[i][1]]
            i += 1
            
        return min_cnt
                    
            
        