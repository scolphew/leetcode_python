import sys


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg, pos, maxp = 1, 1, -sys.maxsize - 1
        for n in nums:
            if n < 0:
                neg, pos = min(n, pos * n), neg * n
            else:
                neg, pos = neg * n, max(n, pos * n)
            maxp = max(maxp, pos)
        return maxp


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([1, 2, 3, 4, 5]))
