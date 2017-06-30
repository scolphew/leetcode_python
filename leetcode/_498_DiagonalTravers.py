class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        n = len(matrix)
        m = len(matrix[0])
        ans = [0] * (m * n)
        dirs = ((-1, 1), (1, -1))
        x = 0
        y = 0
        d = 0
        for i in range(m * n):
            ans[i] = matrix[x][y]
            x += dirs[d][0]
            y += dirs[d][1]

            if x >= n:
                x = n - 1
                y += 2
                d = 1 - d
            if y >= m:
                y = m - 1
                x += 2
                d = 1 - d
            if y < 0:
                y = 0
                d = 1 - d
            if x < 0:
                x = 0
                d = 1 - d

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findDiagonalOrder([[1, 2, 3], [4, 5, 6]]))
