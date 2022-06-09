import itertools
from typing import List


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:  # noqa
        same = {a for a, b in zip(fronts, backs) if a == b}
        seq = set(x for x in fronts + backs if x not in same)
        return min(seq) if seq else 0


if __name__ == '__main__':
    s = Solution()
    y = s.flipgame(fronts=[1, 2, 4, 4, 7], backs=[1, 3, 4, 1, 3])
    print(y)
