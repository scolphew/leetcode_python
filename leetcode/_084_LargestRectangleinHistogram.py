class Solution(object):
    def largestRectangleArea(self, heights):
        """
        求直方图中最大矩形面积
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        max_area = 0
        heights.append(0)
        i = 0
        stack = []
        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
                continue
            top_idx = stack.pop()
            area = heights[top_idx] * (i if not stack else (i - stack[-1] - 1))
            max_area = area if area > max_area else max_area
        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
