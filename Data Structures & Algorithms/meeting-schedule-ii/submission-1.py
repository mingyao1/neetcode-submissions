"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0        
        res = 0
        cur = 0
        start = []
        end = []

        for i in intervals:
            s, e = i.start, i.end
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()
        sp, ep = 0, 0

        while ep < len(intervals):
            while sp < len(intervals) and start[sp] < end[ep]:
                cur += 1
                sp += 1
                res = max(res, cur)
            cur -= 1
            ep += 1
        
        return res
            

