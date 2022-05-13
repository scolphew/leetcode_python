import itertools
import pprint
from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:  # noqa
        def g(word):
            return zip(*[(k, len(list(grp)))
                         for k, grp in itertools.groupby(word)])

        ans = 0
        chars, nums = g(s)
        for w in words:
            chars_w, nums_w = g(w)
            if chars != chars_w:
                continue
            ans += all(c1 >= max(c2, 3) or c1 == c2
                       for c1, c2 in zip(nums, nums_w))
        return ans


if __name__ == '__main__':
    s = Solution()
    s.expressiveWords("aaaaabbccc", 1)
