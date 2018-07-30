"""
最长上升子序列
https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        给定一个无序的整数数组，找到其中最长上升子序列的长度。
        可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
        算法的时间复杂度降低到 O(n log n)

        :type nums: List[int] 整数数组
        :rtype: int 最长上升子序列的长度

        >>> s = Solution()
        >>> s.lengthOfLIS([10,9,2,5,3,7,101,18])
        4
        >>> s.lengthOfLIS([1,2,3,4,5,6,7,8])
        8
        """
        import bisect
        dp = [0] * len(nums)
        len_ = 0
        for num in nums:
            index = bisect.bisect_left(dp, num, 0, len_)
            dp[index] = num
            if index == len_:
                len_ += 1
        return len_


if __name__ == '__main__':
    import doctest

    doctest.testmod()
