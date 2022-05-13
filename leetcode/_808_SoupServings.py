import math
from functools import cache


class Solution:
    def soupServings(self, n: int) -> float:  # NOQA
        n = math.ceil(n / 25)
        if n > 200:
            return 1

        @cache
        def dp(x, y):
            if x <= 0 or y <= 0:
                if x <= 0 and y <= 0:
                    return 0.5  # 同时分配完，乘以0.5
                elif x <= 0:
                    return 1  # a 先分配完
                else:
                    return 0  # b 先分配完
            else:
                return 0.25 * (dp(x - 4, y) + dp(x - 3, y - 1) + dp(x - 2, y - 2) + dp(x - 1, y - 3))

        return dp(n, n)


if __name__ == '__main__':
    s = Solution()
    xx = s.soupServings(10)
    print(xx)
