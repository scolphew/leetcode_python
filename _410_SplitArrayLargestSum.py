class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        import sys
        dp = [[sys.maxsize] * m for _ in range(len(nums))]
        dp[0][0] = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = nums[i] + dp[i - 1][0]
        for i in range(len(nums)):
            for j in range(1, min(i + 1, m)):
                if i == j:
                    dp[i][j] = max(nums[:i + 1])
                    break
                avg = dp[i][0] / (j + 1)
                for i_ in range(i - 1, -1, -1):
                    if dp[i][0] - dp[i_][0] == avg:
                        dp[i][j] = dp[i_][j - 1]
                        break
                    elif dp[i][0] - dp[i_][0] > avg:
                        if i_ <= i:
                            dp[i][j] = min(dp[i][j], max(dp[i_][j - 1], dp[i][0] - dp[i_][0]))
                        i_ += 1
                        if i_ <= i:
                            dp[i][j] = min(dp[i][j], max(dp[i_][j - 1], dp[i][0] - dp[i_][0]))
                        break
                else:
                    dp[i][j] = min(dp[i][j], max(dp[i_][0], dp[i][0] - dp[i_][0]))
        for i in dp:
            print(i)
        return dp[-1][-1]


s = Solution()
a = [10, 2, 3]
m = 2
# print(len(a), 27407869)
print(s.splitArray(a, m))
