class Solution(object):
    def minPathSum(self, grid):
        """
        m，n的最短路径事数量（加权）
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        result = [grid[0][0]]
        for i in range(1, n):
            result.append(grid[0][i] + result[i - 1])
        for i in range(1, m):
            result[0] += grid[i][0]
            for j in range(1, n):
                result[j] = min(result[j], result[j - 1]) + grid[i][j]
        return result[-1]


if __name__ == '__main__':
    s = Solution()
    a = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    print(s.minPathSum(a))
