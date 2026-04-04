"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = [], []

        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        sp, ep = 0, 0
        count = 0
        curr = 0

        while sp < len(intervals):
            if start[sp] < end[ep]:
                curr += 1
                sp += 1
            else:
                curr -= 1
                ep += 1
            count = max(count, curr)
            
            
        return count

