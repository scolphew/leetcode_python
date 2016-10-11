class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[-1][-1] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        result = [0] * n
        for i in range(n):
            if obstacleGrid[0][i]:
                break
            result[i] = 1

        for i in range(1, m):
            result[0] *= (1 - obstacleGrid[i][0])
            for j in range(1,n):
                result[j] = 0 if obstacleGrid[i][j] else result[j] + result[
                    j - 1]
        return result[-1]


s = Solution()
print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
