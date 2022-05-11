from typing import List


class UnionFind:
    """
    并查集
    """

    def __init__(self, n: int):
        self.parent: List[int] = [i for i in range(n)]
        self.size: List[int] = [1 for i in range(n)]

    def find(self, x: int):
        """
        路径压缩，只要求每个不相交集合的「根结点」的子树包含的结点总数数值正确即可，
        因此在路径压缩的过程中不用维护数组 size
        """
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]

    def get_size(self, x: int):
        return self.size[self.find(x)]


class Solution:

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:  # noqa
        """
        有一个 m x n 的二元网格  grid  ，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是：
        一块砖直接连接到网格的顶部，或者
        至少有一块相邻（4  个方向之一）砖块 稳定 不会掉落时
        给你一个数组 hits ，这是需要依次消除砖块的位置。
        每当消除  hits[i] = (rowi, coli) 位置上的砖块时，对应位置的砖块（若存在）会消失
        然后其他的砖块可能因为这一消除操作而 掉落 。
        一旦砖块掉落，它会 立即 从网格  grid  中消失（即，它不会落在其他稳定的砖块上）。

        返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。
        注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。
        """
        m, n = len(grid), len(grid[0])
        res = []
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        # 原始数组复制
        copy_grid = [[_ for _ in rows] for rows in grid]
        # 删除每一步中的方块
        for i, j in hits:
            copy_grid[i][j] = 0
        # 初始化并查集
        size = m * n
        union_find = UnionFind(size + 1)

        # 构建并查集
        def get_index(_x: int, _y: int):
            return _x * n + _y

        def in_area(_x: int, _y: int):
            return 0 <= _x < m and 0 <= _y < n

        # 1. 第一行与屋顶相连
        for i, brick in enumerate(copy_grid[0]):
            if brick == 1:
                union_find.union(i, size)  # size 表示屋顶
        # 每一个砖块与上/坐相连
        for i, row in enumerate(copy_grid[1:], 1):
            for j, brick in enumerate(row):
                if brick == 1:
                    # 如果上方是砖块
                    if copy_grid[i - 1][j] == 1:
                        union_find.union(get_index(i, j), get_index(i - 1, j))
                    # 如果左边是砖块
                    if j > 0 and copy_grid[i][j - 1] > 0:
                        union_find.union(get_index(i, j), get_index(i, j - 1))
        # 按照 hits 的逆序，将砖块补回
        for x, y in reversed(hits):
            # 原本就没有砖块，跳过
            if grid[x][y] == 0:
                res.append(0)
                continue
            origin = union_find.get_size(size)  # 与屋顶连接的数量
            if x == 0:  # 如果该砖块在第一行，与屋顶相连
                union_find.union(y, size)
            # 四个方向合并并查集
            for delta_x, delta_y in directions:
                new_x, new_y = x + delta_x, y + delta_y
                if in_area(new_x, new_y) and copy_grid[new_x][new_y] == 1:
                    union_find.union(get_index(x, y), get_index(new_x, new_y))
            current = union_find.get_size(size)  # 合并后与屋顶连接的数量
            res.append(max(0, current - origin - 1))
            copy_grid[x][y] = 1
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    xx = s.hitBricks([[1, 0, 1], [0, 0, 1]], hits=[[1, 0], [0, 0]])
    print(xx)
