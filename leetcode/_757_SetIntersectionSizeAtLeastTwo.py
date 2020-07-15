from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[1], -x[0]))

        p1, p2 = intervals[0][1] - 1, intervals[0][1]
        ans = 2

        for a, b in intervals[1:]:
            if a <= p1:
                continue
            if a <= p2:
                p1, p2 = p2, b
                ans += 1
            else:
                p1, p2 = b - 1, b
                ans += 2
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.intersectionSizeTwo(
        [[3, 13], [2, 8], [5, 10]]
    ))
