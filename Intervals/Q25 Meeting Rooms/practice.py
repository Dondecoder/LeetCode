# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
"""

class Solution:
    def canAttendMeetings(self, intervals:Interval):
        intervals.sort(key = lambda i : i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True


Meeting_Room = Solution()
Meeting_Room.canAttendMeetings([Interval(5,8),Interval(9,15),Interval(15,20)])


