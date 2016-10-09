from interval import *


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: interval
        :rtype: List[Interval]
        """

        def search(target, data):
            l, h = 0, len(data) - 1
            while l <= h:
                mid = (l + h) >> 1
                s, e = data[mid].start, data[mid].end
                if s <= target <= e:
                    return mid
                elif target < s:
                    h = mid - 1
                else:
                    l = mid + 1
            return l

        s, e = newInterval.start, newInterval.end
        left = search(s, intervals)
        right = search(e, intervals)
        if left < len(intervals) and intervals[left].start <= s <= intervals[left].end:
            start = intervals[left].start
        else:
            start = s
        if right < len(intervals) and intervals[right].start <= e <= intervals[right].end:
            end = intervals[right].end
            right += 1
        else:
            end = e
        return intervals[:left] + [Interval(start, end)] + intervals[right:]


s = Solution()
a = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
print(s.insert(get_intervals(a), Interval(4, 9)))
a = [[1, 5]]
print(s.insert(get_intervals(a), Interval(2, 3)))
a = [[1, 5]]
print(s.insert(get_intervals(a), Interval(0, 0)))
