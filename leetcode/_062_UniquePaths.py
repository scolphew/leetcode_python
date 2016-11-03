from functools import reduce


class Solution(object):
    def uniquePaths(self, m, n):
        """
        m，n的最短路径事数量
        :type m: int
        :type n: int
        :rtype: int
        """
        result = 1
        for i in range(1, m):
            result = result * (m + n - 1 - i) / i
        return result

    def d2(self, m, n):
        result = [[1] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                result[i][j] = result[i - 1][j] + result[i][j - 1]
        return result[n - 1][m - 1]

    def d3(self, m, n):
        import math
        return math.factorial(m + n - 2) / math.factorial(
            m - 1) / math.factorial(n - 1)

    def d4(self, m, n):
        import math
        import operator
        return reduce(operator.mul, range(n, m + n - 1), 1) / reduce(
            operator.mul, range(1, m), 1)


s = Solution()
print(s.uniquePaths(11, 11))
print(s.d4(1, 2))
