"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""


class Solution(object):
    def numDecodings(self, s):
        """
        计算数字序列能转换成几种字母序列
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        dp = [1]
        for i in range(1, len(s)):
            dp.append(0 if s[i] == '0' else dp[i - 1])
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                dp[i] += dp[i - 2] if i > 1 else 1
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("10"))
