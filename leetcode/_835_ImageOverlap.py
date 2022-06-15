import collections
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:  # noqa
        count = collections.defaultdict(int)
        for i, row in enumerate(img1):
            for j, v in enumerate(row):
                if v:
                    for i2, row2 in enumerate(img2):
                        for j2, v2 in enumerate(row2):
                            if v2:
                                count[i2 - i, j2 - j] += 1
        return max(count.values() or [0])
