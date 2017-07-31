class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import deque
        n, m = len(matrix), len(matrix[0])
        ans = [[0xffffffff] * m for _ in range(n)]

        q = deque()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    q.append((i, j))
                    ans[i][j] = 0
        while q:
            i, j = q.popleft()
            d = ans[i][j]
            for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if 0 <= i + x < n and 0 <= j + y < m and ans[i + x][
                            j + y] > d + 1:
                    ans[i + x][j + y] = d + 1
                    q.append((i + x, j + y))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.updateMatrix([
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1],
    ]))
