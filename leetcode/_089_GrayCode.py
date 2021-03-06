"""
格雷码
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits
in the code, print the sequence of gray code. A gray code sequence
must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
"""


class Solution(object):
    def grayCode(self, n):
        """
        格雷码
        :type n: int
        :rtype: List[int]
        """
        if not n:
            return [0]
        result = [0, 1]
        x = 1
        for _ in range(1, n):
            x <<= 1
            result.extend([j + x for j in result[::-1]])
        return result

    def d2(self, n):
        res = []
        for i in range(2 ** n):
            res.append((i >> 1) ^ i)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.grayCode(5))
    print(s.d2(5))
