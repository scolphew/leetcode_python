class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 1:
            return 1
        if n == 1:
            return x
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)

        if not n % 2:
            xx = self.myPow(x, n // 2)
            return xx * xx
        else:
            return x * self.myPow(x, n - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(8.88023, 3))
