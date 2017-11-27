#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        d = defaultdict(int)
        for each in wall[:-1]:
            left = 0
            for i in each:
                left += i
                d[left] += 1
        ans = 0
        for i in d.values():
            ans = max(ans, i)
        return len(wall) - ans


if __name__ == '__main__':
    s = Solution()
    print(s.leastBricks(
        [
            [1, 2, 3],
            [1, 2, 3],
        ]
    ))
