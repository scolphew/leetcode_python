"""
    一个矩阵，给出举矩阵中面积最大的全为1的子矩阵
    Given a 2D binary matrix filled with 0's and 1's,
    find the largest rectangle containing only 1's and return its area.
    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0
    -> 6
    解法参考上一题，将每一行转换为直方图（每个位置的盖度为向上的1的累积个数），然后每一行求最大面积
    遍历每一行
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            i = 0
            stack = []
            while i < n + 1:
                if not stack or height[i] >= height[stack[-1]]:
                    stack.append(i)
                    i += 1
                    continue
                top_idx = stack.pop()
                area = height[top_idx] * (
                    i if not stack else (i - stack[-1] - 1))
                ans = area if area > ans else ans
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maximalRectangle(["10100", "10111", "11111", "10010"]))
