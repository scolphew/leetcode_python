"""
Given two integers n and k, return all possible combinations of k numbers
out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        currrent = []
        j = 1
        while True:
            l = len(currrent)
            if l == k:
                result.append(currrent[:])
            if l == k or j > n - k + l + 1:
                if not currrent:
                    return result
                j = currrent.pop() + 1
                continue
            currrent.append(j)
            j += 1


s = Solution()
print(s.combine(4, 2))
