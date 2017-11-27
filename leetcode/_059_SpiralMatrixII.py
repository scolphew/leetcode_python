class Solution(object):
    def generateMatrix(self, n):
        """
        螺旋矩阵
        给一个数字，写出螺旋矩阵
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0] * n for _ in range(n)]
        elems = iter(range(1, n ** 2 + 1))
        for i in range(n // 2 + 1):
            for j in range(i, n - i):
                result[i][j] = next(elems)
            for j in range(i + 1, n - i):
                result[j][n - i - 1] = next(elems)
            for j in range(i + 1, n - i):
                result[n - i - 1][n - j - 1] = next(elems)
            for j in range(i + 1, n - i - 1):
                result[n - j - 1][i] = next(elems)
        print(result)


if __name__ == '__main__':
    s = Solution()
    s.generateMatrix(4)
    s.generateMatrix(5)
