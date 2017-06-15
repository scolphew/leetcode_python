class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if (i > 0 and grid[i - 1][j] == 1) and (
                                    j > 0 and grid[i][j - 1] == 1):
                        continue
                    elif (i > 0 and grid[i - 1][j] == 1) or (
                                    j > 0 and grid[i][j - 1] == 1):
                        ans += 2
                    else:
                        ans += 4

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.islandPerimeter([
        [0],
        [1],
    ]))
