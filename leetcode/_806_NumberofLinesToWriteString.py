from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:  # noqa
        MAX_WIDTH = 100  # noqa
        row, col = 1, 0
        for c in s:
            width = widths[ord(c) - ord('a')]
            col += width
            if col > MAX_WIDTH:
                row += 1
                col = width
        return [row, col]
