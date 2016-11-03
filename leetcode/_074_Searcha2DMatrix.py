class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        二维矩阵搜索
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m - 1
        while l <= r:
            mid_1 = (l + r) >> 1
            if matrix[mid_1][0] <= target <= matrix[mid_1][n - 1]:
                break
            elif target > matrix[mid_1][n - 1]:
                l = mid_1 + 1
            else:
                r = mid_1 - 1
        else:
            return False

        l, r = 0, n - 1
        while l <= r:
            mid_2 = (l + r) >> 1
            if matrix[mid_1][mid_2] == target:
                return True
            elif target > matrix[mid_1][mid_2]:
                l = mid_2 + 1
            else:
                r = mid_2 - 1
        else:
            return False

    def searchMatrix2(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) >> 1
            i, j = mid // n, mid % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                r = mid - 1
            else:
                l = mid + 1
        else:
            return False


s = Solution()
print(s.searchMatrix2([[1, 3]], 3))
print(s.searchMatrix(
    [[-8, -8, -7, -7, -6, -5, -3, -2],
     [0, 0, 1, 3, 4, 6, 8, 8],
     [11, 12, 14, 16, 18, 18, 19, 19],
     [22, 23, 25, 27, 28, 30, 30, 31],
     [34, 35, 37, 39, 40, 42, 43, 45],
     [48, 50, 51, 51, 53, 54, 55, 57],
     [58, 60, 62, 62, 62, 63, 63, 65],
     [68, 69, 71, 72, 72, 72, 74, 76]]
    , 76))
