class Solution(object):
    def setZeroes(self, matrix):
        """
        矩阵，若某个数为0，将改行该列全换位0
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row_zero = False
        for i in matrix:
            if i[0] == 0:
                row_zero = True
                break

        col_zero = False
        for j in matrix[0]:
            if j == 0:
                col_zero = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        if col_zero:
            for j in range(n):
                matrix[0][j] = 0
        if row_zero:
            for i in range(m):
                matrix[i][0] = 0


if __name__ == '__main__':
    s = Solution()
    a = [
        [1, 2, 3],
        [4, 0, 6]
    ]
    s.setZeroes(a)
    print(a)
