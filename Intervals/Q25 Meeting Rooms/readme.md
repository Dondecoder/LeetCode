# Name

920 Meeting Rooms

## Problem

* Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

## Solution

* For this problem the first thing we need to do is sort the array by start times use a lambda function within the sort built-in list method and sort by start times. Iterate using a for loop starting from index 1 then check if the the first elements end is > then the next elements start time. If it is return False. Else return True

```python
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key=lambda x: x.start)

        for i in range(1,len(intervals)):
            meet_1 = intervals[i-1]
            meet_2 = intervals[i]

            if meet_1.end > meet_2.start:
                return False
        return True
```