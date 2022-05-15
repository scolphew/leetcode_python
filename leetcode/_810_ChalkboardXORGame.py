from functools import reduce
from operator import xor
from typing import List


class Solution:
    def xorGame(self, nums: List[int]) -> bool:  # noqa
        return reduce(xor, nums) == 0 or (len(nums) & 1) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.xorGame([1, 2, 3]))
