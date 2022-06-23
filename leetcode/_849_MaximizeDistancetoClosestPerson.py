import itertools
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:  # noqa
        ans = 0
        i, n = 0, len(seats)
        p = -1
        while i < n:
            while i < n and seats[i] == 0:
                i += 1
            if p == -1:
                ll = i
            else:
                ll = (n - p - 1) if i == n else (i - p) >> 1
            ans = max(ans, ll)
            p = i
            i += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    y = s.maxDistToClosest([1, 0, 1])
    print(y)
