class Solution(object):
    def minMeetingRooms(self, intervals):
        dt = {}
        intervals.sort(key=lambda x: x[1])
        dt[1] = intervals[0][1]
        lind = 1
        ilen = len(intervals)
        for i in range(1,ilen):
            sml = 1000001
            x = 0
            for j in dt:
                if intervals[i][0] >= dt[j]: 
                    if sml > intervals[i][0] - dt[j]: 
                        sml = intervals[i][0] - dt[j]
                        x = j        
            if sml == 1000001:
                lind += 1
                dt[lind] = intervals[i][1]
            else: dt[x] =  intervals[i][1]
        return lind
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        