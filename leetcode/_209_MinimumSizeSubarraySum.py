class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        求nums的子数组和为s，的子数组的最短长度。没有则返回0
        所有数值均为正数
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        sum = 0
        i, j = 0, 0
        res = l + 1
        while sum < s:
            sum += nums[j]
            j += 1
            while sum >= s:
                if j - i < res:
                    res = j - i
                sum -= nums[i]
                i += 1
            if j == l:
                break
        return 0 if res > l else res


if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
