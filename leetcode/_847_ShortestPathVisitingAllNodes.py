from typing import List
from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:  # noqa
        n = len(graph)
        # 广度优先
        # q: (当前位置，以访问过的结点，当前路径长度)
        q = deque((i, 1 << i, 0) for i in range(n))
        visited = set((i, 1 << i) for i in range(n))
        ans = 0

        while q:
            u, mask, dist = q.popleft()
            if mask == (1 << n) - 1:
                ans = dist
                break
            # 搜索相邻的节点
            for v in graph[u]:
                # 将 mask 的第 v 位置为 1
                mask_v = mask | (1 << v)
                if (v, mask_v) not in visited:
                    q.append((v, mask_v, dist + 1))
                    visited.add((v, mask_v))

        return ans


if __name__ == "__main__":
    s = Solution()
    y = s.shortestPathLength([[1, 2, 3], [0], [0], [0]])
    print(y)
