class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        for i in ops:
            m = min(m, i[0])
            n = min(n, i[1])
        return m * n
