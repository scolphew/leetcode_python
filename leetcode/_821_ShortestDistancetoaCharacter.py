from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:  # noqa
        n = len(s)
        ans = [0] * n

        idx = -n
        for i, ch in enumerate(s):
            if ch == c:
                idx = i
            ans[i] = i - idx

        idx = 2 * n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                idx = i
            ans[i] = min(ans[i], idx - i)
        return ans
