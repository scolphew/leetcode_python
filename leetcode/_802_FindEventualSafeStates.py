from collections import deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:  # noqa
        def explore(x):
            visited[x] = 0
            for v in graph[x]:
                if visited[v] == 0 or (visited[v] == -1 and explore(v)):
                    return True
            visited[x] = 1
            res.append(x)
            return False

        visited, res = [-1] * len(graph), []
        for i in range(len(graph)):
            if visited[i] == -1:
                explore(i)
        return sorted(res)
