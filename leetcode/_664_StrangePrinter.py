class Solution:
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        def f(i, j):
            if i > j:
                return 0
            if dp[i][j] == 0:
                ans = f(i + 1, j) + 1
                for x in range(i + 1, j + 1):
                    if s[x] == s[i]:
                        ans = min(ans, f(i, x - 1) + f(x + 1, j))
                dp[i][j] = ans
            return dp[i][j]

        return f(0, n - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.strangePrinter("ababcba"))
