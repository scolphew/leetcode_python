from typing import List
from collections import defaultdict


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:  # noqa
        """
        给定你一个整数数组 nums
        我们要将 nums 数组中的每个元素移动到 A 数组 或者 B 数组中，
        使得 A 数组和 B 数组不为空，并且 average(A) == average(B) 。
        如果可以完成则返回true ， 否则返回 false  。
        注意：对于数组 arr ,  average(arr) 是 arr 的所有元素除以 arr 长度的和。

        """
        sum_ = sum(nums)
        N = len(nums)
        if N < 2:
            return False
        if sum_ == 0:
            return True
        nums.sort()
        # dp[i,j] : 前i个（0开始）和为 j 时可能存在的元素个数
        # 如 dp[2,3]=3=0b11 表示nums[0:2]里，和为3的子序列长度可以为1和2
        dp = [[0 for _ in range(N * nums[-1])] for _ in range(N)]
        s = nums[0]
        dp[0][nums[0]] = 1
        for i in range(1, N):
            s += nums[i]
            for j in range(s + 1):
                dp[i][j] = dp[i - 1][j]
                # if j == nums[i]:  # 子序列只有1个 即nums[i]
                #     dp[i][j] |= 1
                if j >= nums[i]:
                    # 两种情况相加
                    dp[i][j] |= dp[i - 1][j - nums[i]] << 1
                if j > 0 and j * N % sum_ == 0 and j * N // sum_ < N and (dp[i][j]) & (1 << (j * N // sum_ - 1)):
                    return True
        return False

    def splitArraySameAverage2(self, nums: List[int]) -> bool:  # noqa
        n = len(nums)
        if n == 1:
            return False
        sum_ = sum(nums)
        #  (new的平均值为0)
        # 转化为求 new 数组的两个子序列和为0
        new = [num * n - sum_ for num in nums]
        left_len = n // 2
        right_len = n - n // 2
        left_sum = [0] * (1 << left_len)  # 左半部分子序列和
        right_sum = [0] * (1 << right_len)  # 右半部分子序列和
        for i in range(1, 1 << left_len):  # i=0x101 表示取left 0,2位置求和
            for j in range(left_len):
                if i & 1 << j:  # 位运算
                    left_sum[i] = left_sum[i - (1 << j)] + new[j]
                    break
        for i in range(1, 1 << right_len):
            for j in range(left_len, n):
                if i & 1 << (j - left_len):
                    right_sum[i] = right_sum[i - (1 << (j - left_len))] + new[j]
                    break
        left, right = set(left_sum[1:]), set(right_sum[1:])  # 需要排除首位，空集
        for l_sum in left:
            if l_sum == 0:  # 左半边有和为0的子序列
                return True
            if - l_sum in right and not (l_sum == left_sum[-1] and - l_sum == right_sum[-1]):
                # 左右和为0 且不能均为全集
                return True
        for r_sum in right:
            if r_sum == 0:
                return True
            if - r_sum in left and not (r_sum == right_sum[-1] and - r_sum == left_sum[-1]):
                return True
        return False


if __name__ == '__main__':
    ss = Solution()
    yy = ss.splitArraySameAverage2([2, 0, 7, 0, 6])
    print(yy)
