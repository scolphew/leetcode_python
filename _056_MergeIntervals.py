from interval import Interval


class Solution(object):
    def merge(self, intervals):
        """
        合并连续的区间
        时间nlogn
        如：[1,3],[2,6],[8,10],[15,18]->[1,6],[8,10],[15,18]
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        if not intervals:
            return result
        intervals.sort(key=lambda a: a.start)
        s = intervals[0].start
        e = intervals[0].end
        for i in intervals:
            if i.start <= e:
                e = max(i.end, e)
            else:
                result.append(Interval(s, e))
                s = i.start
                e = i.end
        result.append(Interval(s, e))
        return result


s = Solution()
a = [[1, 3], [2, 6], [8, 10], [5, 7], [15, 18]]
b = []
for x in a:
    b.append(Interval(x[0], x[1]))
print(s.merge(b))
