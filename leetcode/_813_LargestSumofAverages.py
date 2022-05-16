from functools import cache
from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:  # noqa
        P = [0]
        for x in nums:
            P.append(P[-1] + x)

        @cache
        def average(i, j):
            return (P[j] - P[i]) / float(j - i)

        N = len(nums)
        dp = [average(i, N) for i in range(N)]
        for k in range(k - 1):
            for i in range(N):
                for j in range(i + 1, N):
                    dp[i] = max(dp[i], average(i, j) + dp[j])

        return dp[0]


if __name__ == '__main__':
    s = Solution()
    s.largestSumOfAverages([9, 1, 2, 3, 9], 3)
