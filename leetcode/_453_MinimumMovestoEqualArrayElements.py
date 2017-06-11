from functools import reduce


class Solution(object):
    def minMoves(self, nums):
        """
        非空数组，求经过多少次变换后所有值相等（每次变换为把n-1个数+1）
        解法：
        sum + m * (n-1) = n * x   m=变换次数 x=最终值        
        x = min + m (最小值每次都加，所以最终的值为最小变换次数)
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.minMoves([2, 3, 3]))
