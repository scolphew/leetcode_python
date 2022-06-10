from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:  # noqa
        n = len(grid)
        areas = {}
        index = 100

        def dfs(a, b):
            grid[a][b] = index
            ans = 1
            for delta_x, delta_y in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                new_a, new_b = a + delta_x, b + delta_y
                if 0 <= new_a < n and 0 <= new_b < n and grid[new_a][new_b] == 1:
                    ans += dfs(new_a, new_b)
            return ans

        max_area = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    index += 1
                    areas[index] = dfs(i, j)
                    max_area = max(max_area, areas[index])

        for i in range(n):
            for j in range(n):
                se = set()
                if grid[i][j] == 0:
                    for delta_i, delta_j in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                        new_i, new_j = i + delta_i, j + delta_j
                        if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] > 100:
                            se.add(grid[new_i][new_j])
                max_area = max(max_area, 1 + sum(areas[e] for e in se))
        return max_area


if __name__ == '__main__':
    s = Solution()
    y = s.largestIsland([[1, 0], [0, 1]])
    print(y)
