from typing import List
from collections import defaultdict, deque


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:  # noqa
        d = defaultdict(list)  # 直接比自己钱少的
        n = len(quiet)
        richer_count = [0 for _ in range(n)]  # 直接比自己钱多的人数量
        for a, b in richer:
            d[a].append(b)
            richer_count[b] += 1

        ans: list[int] = list(range(n))
        q: deque[int] = deque(i for i, p in enumerate(richer_count) if p == 0)  # 没有比自己更有钱的人

        while q:
            x: int = q.popleft()
            for person in d[x]:
                if quiet[ans[person]] > quiet[ans[x]]:
                    ans[person] = ans[x]
                richer_count[person] -= 1
                if richer_count[person] == 0:
                    q.append(person)

        return ans


if __name__ == "__main__":
    s = Solution()
    y = s.loudAndRich([[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]], quiet=[3, 2, 5, 4, 6, 1, 7, 0])
    print(y)
