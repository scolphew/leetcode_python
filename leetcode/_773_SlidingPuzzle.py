from typing import List
from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        t = tuple(str(e) for r in board for e in r)
        s = "".join(t)
        target = "123450"

        if s == target:
            return 0
        change = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

        visited = set()
        q = deque([s])
        ans = 0
        while q:
            ans += 1
            for _ in range(len(q)):
                element = q.popleft()
                i = element.index("0")
                for j in change[i]:
                    new = list(element)
                    new[i], new[j] = new[j], new[i]
                    s = "".join(new)
                    if s == target:
                        return ans
                    if s not in visited:
                        visited.add(s)
                        q.append(new)
        return -1
