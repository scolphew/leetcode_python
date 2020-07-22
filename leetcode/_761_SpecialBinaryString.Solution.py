"""
特殊的二进制序列是具有以下两个性质的二进制序列：

0 的数量与 1 的数量相等。
二进制序列的每一个前缀码中 1 的数量要大于等于 0 的数量。
给定一个特殊的二进制序列 S，以字符串形式表示。定义一个操作为首先选
择S的两个连续且非空的特殊的子串，然后将它们交换。（两个子串为连续的
当且仅当第一个子串的最后一个字符恰好为第二个子串的第一个字符的前一
个字符。)

在任意次数的操作之后，交换后的字符串按照字典序排列的最大的结果是什么？


对于字符串S,将1视为上升，2视为下降
则1100111000可以表示为

          /\
     /\  /  \
    /  \/    \

同意高度的相邻山峰可以交换。（相当于排序，把连续上升多的放到前面）

同时，对于下列情况

          /\
     /\  /  \
    /  \/    \
   /          \
因为每个字串都是1开头，0结尾，每次递归调用子串掐头去尾
"""


class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        start = ans = 0
        lst = []
        for i, c in enumerate(S):
            ans += 1 if c == '1' else -1
            if ans == 0:
                lst.append("1" + self.makeLargestSpecial(S[start + 1:i]) + "0")
                start = i + 1
        return "".join(sorted(lst)[::-1])


if __name__ == '__main__':
    s = Solution()
    print(s.makeLargestSpecial("1100111000"))
