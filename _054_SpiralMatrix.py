class Solution(object):
    def spiralOrder(self, matrix):
        """
        螺旋输出矩阵
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        n = len(matrix)
        m = len(matrix[0])
        count = m * n
        max_c = min(m, n) + 1 >> 1
        result = []
        detal = lambda i, j: (i, j + 1)
        delta_key = "right"
        delta_dict = {
            "right": ("down", lambda i, j: (i + 1, j)),
            "down": ("left", lambda i, j: (i, j - 1)),
            "left": ("up", lambda i, j: (i - 1, j)),
            "up": ("right", lambda i, j: (i, j + 1)),
        }

        i = j = 0
        c = 1
        count_1 = 0
        while c <= max_c and count_1 < count:
            result.append(matrix[i][j])
            print(result)
            if (delta_key == "right" and j == m - c) or (
                            delta_key == "down" and i == n - c) or (
                            delta_key == "left" and j == c - 1):
                delta_key, detal = delta_dict[delta_key]
            elif delta_key == "up" and i == c:
                delta_key, detal = delta_dict[delta_key]
                c += 1
            i, j = detal(i, j)
            count_1 += 1
        return result


s = Solution()
s.spiralOrder(
    [
        [1, 2, 3, 4],
        [4, 5, 6, 5],
        [7, 8, 9, 6]
    ]
)
