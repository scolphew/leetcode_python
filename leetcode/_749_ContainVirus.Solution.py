from typing import List
from collections import defaultdict


class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(i, j):
            if visited[i][j] == 0:
                # 如果是未访问的
                if grid[i][j] == 1:
                    visited[i][j] = 1
                    # 标记区域访问
                    # 遍历四个方向
                    for x, y in directions:
                        x, y = i + x, j + y
                        if 0 <= x < m and 0 <= y < n:
                            dfs(x, y)
                            district[index].add((i, j))
                elif grid[i][j] == 0:
                    border[index].add((i, j))
                    wall[index] += 1

        ans = 0
        while True:
            visited = [[0] * n for _ in range(m)]
            wall = defaultdict(int)
            border = defaultdict(set)
            district = defaultdict(set)
            index = 1

            max_index, max_border = 0, 0
            for i in range(m):
                for j in range(n):
                    # 对于未访问的病毒区域，开始遍历
                    if grid[i][j] == 1 and visited[i][j] == 0:
                        dfs(i, j)
                        if len(border[index]) > max_border:
                            max_index = index
                            max_border = len(border[index])
                        index += 1

            ans += wall[max_index]

            for i, j in district[max_index]:
                grid[i][j] = -1
            for k in border.keys():
                if k != max_index:
                    for i, j in border[k]:
                        if grid[i][j] == 0:
                            grid[i][j] = 1
            if max_border == 0:
                break

            # for x in grid:
            #     print(x)
            # break

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.containVirus(
        [[1, 1, 1, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 0, 0, 0, 0]]
    ))

    print(s.containVirus(
        [[1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]]
    ))

    print(s.containVirus(
        [[0, 1, 0, 0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0]]
    ))

    print(s.containVirus(
        [[0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
         [0, 1, 0, 0, 1, 0, 1, 1, 0, 1],
         [0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
         [0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
         [0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
         [0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
         [1, 0, 1, 1, 0, 1, 0, 1, 0, 1]]
    ))
    print(s.containVirus(
        [[0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
         [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
         [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
         [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
         [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
         [1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1],
         [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1]]
    ))
