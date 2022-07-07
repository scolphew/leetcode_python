class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:  # noqa
        m, n = len(grid), len(grid[0])
        ans = m * (1 << (n - 1))  # 第一列都是1
        for j in range(1, n):
            ones = 0
            for i in range(m):
                if grid[i][0] == 0:
                    ones += 1 - grid[i][j]
                else:
                    ones += grid[i][j]
            ans += max(ones, m - ones) * (1 << (n - 1 - j))
        return ans


if __name__ == "__main__":
    s = Solution()
    y = s.matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]])
    print(y)
