class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        color, length = [], []
        for box in boxes:
            if color and color[-1] == box:
                length[-1] += 1
            else:
                color.append(box)
                length.append(1)
        M, N = len(color), len(boxes)
        dp = [[[0] * N for _ in range(M)] for _ in range(M)]

        def solve(l, r, k):
            if l > r:
                return 0
            if dp[l][r][k]:
                return dp[l][r][k]
            points = solve(l, r - 1, 0) + (length[r] + k) ** 2
            for i in range(l, r):
                if color[i] == color[r]:
                    points = max(points,
                                 solve(l, i, length[r] + k) + solve(i + 1,
                                                                    r - 1, 0))
            dp[l][r][k] = points
            return points

        return solve(0, M - 1, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]))
