import operator
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:  # noqa
        MOD = 10 ** 9 + 7  # noqa
        N = len(arr)  # noqa
        arr.sort()
        dp = [1] * N
        index = {x: i for i, x in enumerate(arr)}
        for i, x in enumerate(arr):
            for j in range(i):
                if x % arr[j] == 0:  # 整除
                    right = x // arr[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD
        return sum(dp) % MOD


if __name__ == '__main__':
    s = Solution()
    y = s.numFactoredBinaryTrees([2, 4, 16])
    print(y)
