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
        result = []
        detal = [0, 1]
        delta_key = "right"
        delta_dict = {
            "right": ("down", (1, 0)),
            "down": ("left", (0, -1)),
            "left": ("up", (-1, 0)),
            "up": ("right", (0, 1)),
        }
        i = j = 0
        c = 1
        for _ in range(count):
            result.append(matrix[i][j])
            if (delta_key == "right" and j == m - c) or (
                            delta_key == "down" and i == n - c) or (
                            delta_key == "left" and j == c - 1):
                delta_key, detal = delta_dict[delta_key]
            elif delta_key == "up" and i == c:
                delta_key, detal = delta_dict[delta_key]
                c += 1
            i += detal[0]
            j += detal[1]
        return result

    def d2(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        delta_dict = {
            'right': [[0, 1], 'down'],
            'down': [[1, 0], 'left'],
            'left': [[0, -1], 'up'],
            'up': [[-1, 0], 'right']
        }
        delta_key = 'right'
        count = 0
        minI, minJ = 0, 0
        maxI, maxJ = m - 1, n - 1
        i, j = 0, 0
        res = []
        res.append(matrix[i][j])
        count += 1
        while count < m * n:
            if delta_key == 'right':
                maxj = maxJ
            elif delta_key == 'left':
                minj = minJ
            elif delta_key == 'down':
                maxi = maxI
            elif delta_key == 'up':
                mini = minI
            delta, next_delta_key = delta_dict[delta_key]
            while True:
                i, j = i + delta[0], j + delta[1]
                if delta_key == 'right' and j > maxj:
                    minI += 1
                    break
                elif delta_key == 'left' and j < minj:
                    maxI -= 1
                    break
                elif delta_key == 'down' and i > maxi:
                    maxJ -= 1
                    break
                elif delta_key == 'up' and i < mini:
                    minJ += 1
                    break
                res.append(matrix[i][j])
                print("add %i: , count %i" % (matrix[i][j], count))
                count += 1
            i, j = i - delta[0], j - delta[1]
            delta_key = next_delta_key
        return res

    def spiralOrder3(self, matrix):
        if not matrix:
            return []
        n = len(matrix)
        m = len(matrix[0])
        result = []
        i = count = 0
        while True:
            for j in range(i, m - i):
                result.append(matrix[i][j])
                count += 1
            if count == m * n: break
            for j in range(i + 1, n - i):
                result.append(matrix[j][m - i - 1])
                count += 1
            if count == m * n: break
            for j in range(i + 1, m - i):
                result.append(matrix[n - i - 1][m - j - 1])
                count += 1
            if count == m * n: break
            for j in range(i + 1, n - i - 1):
                result.append(matrix[n - j - 1][i])
                count += 1
            if count == m * n: break
            i += 1
        return result


s = Solution()
m, n = 7, 2
elems = iter(range(1, m * n + 1))
matrix = [[next(elems) for _ in range(m)] for _ in range(n)]
print(s.spiralOrder4(matrix))

