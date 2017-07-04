class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        dp = [1] * n
        for i in range(1, n):
            pro = 1
            for j in range(i - 1, -1, -1):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = 2 + pro if j <= i - 2 else 2
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                pro = tmp
        return dp[0]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindromeSubseq("bbbab"))
    print(s.longestPalindromeSubseq(""))
    print(s.longestPalindromeSubseq("a"))
    print(s.longestPalindromeSubseq("aa"))
