from typing import List


class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        banned = {tuple(mine) for mine in mines}
        dp = [[0] * N for _ in range(N)]
        ans = 0

        for r in range(N):
            # 左
            count = 0
            for c in range(N):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = count

            # 右
            count = 0
            for c in range(N - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count)

        for c in range(N):
            # 上
            count = 0
            for r in range(N):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count)

            # 下
            count = 0
            for r in range(N - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count)
                ans = max(ans, dp[r][c])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.orderOfLargestPlusSign(5, [[4, 2]]))
