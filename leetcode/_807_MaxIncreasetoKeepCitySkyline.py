from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:  # noqa
        n = len(grid)
        max_x, max_y = [0 for i in range(n)], [0 for i in range(n)]
        for i, row in enumerate(grid):
            for j, h in enumerate(row):
                max_x[i] = max(max_x[i], h)
                max_y[j] = max(max_y[j], h)
        ans = 0
        for i, row in enumerate(grid):
            for j, h in enumerate(row):
                ans += min(max_x[i], max_y[j]) - h
        return ans


if __name__ == '__main__':
    gridNew = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    x = Solution().maxIncreaseKeepingSkyline(gridNew)
    print(x)
