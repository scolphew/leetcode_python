class Solution(object):
    def rotate(self, matrix):
        """
        顺时针旋转矩阵

        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        index = 0
        length = end = len(matrix) - 1
        while index < end:
            i = index
            while i < end:
                x = matrix[index][i]
                matrix[index][i] = matrix[length - i][index]
                matrix[length - i][index] = matrix[length - index][length - i]
                matrix[length - index][length - i] = matrix[i][length - index]
                matrix[i][length - index] = x
                i += 1
            index += 1
            end -= 1


from p import p

s = Solution()

# a = [[1, 2, 3, 4, 5], [5, 6, 7, 8, 9], [9, 10, 11, 12, 13],
#      [13, 14, 15, 16, 17], [17, 18, 19, 20, 21]]
a = [[]]
p(a, 2)
print()
s.rotate(a)
p(a, 2)
