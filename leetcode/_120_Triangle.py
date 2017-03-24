class Solution(object):
    def minimumTotal(self, triangle):
        """
        给一个三角形，找出一条顶部到底部的路径和最小的路径
        [
            [2],
           [3,4],
          [6,5,7],
         [4,1,8,3]
        ]
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        length = len(triangle)
        lst = [0] * length
        lst[0] = triangle[0][0]
        for i in range(1, length):
            lst[i] = lst[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                left = lst[j - 1] + triangle[i][j]
                right = lst[j] + triangle[i][j]
                lst[j] = min(left, right)
            lst[0] = lst[0] + triangle[i][0]

        return min(lst)


if __name__ == '__main__':
    s = Solution()
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(s.minimumTotal(triangle))
