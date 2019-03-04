# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        result = []
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            if result and result[-1].end >= interval.start:
                last = result.pop()
                result.append(Interval(last.start, max(last.end, interval.end)))
            else:
                result.append(interval)
        return result
