import heapq
import time
from functools import cache


class Solution:

    def racecar(self, target: int) -> int:  # noqa
        """
        需要考虑方向
        """

        @cache
        def foo(t: int):
            k = t.bit_length()
            right = (1 << k) - 1
            if t == right:
                return k
            ans = float('inf')
            for i in range(k - 1):
                # A(k-1个) -> R -> A(i个) -> R 共 k-1+1+i+1 此时向右走了 1<<k-1 + 1<<i
                ans = min(ans, k + 1 + i + foo(t - (1 << (k - 1)) + (1 << i)))
            if (1 << k) - 1 - t < t:
                # 先向右走k次，再返回R，之后剩下的
                ans = min(ans, k + 1 + foo(2 ** k - 1 - t))

            return ans

        return foo(target)
