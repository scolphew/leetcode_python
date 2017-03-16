class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while not n % 3:
            n //= 3
        return n == 1

    def f2(self, n):
        return False if n <= 0 else 1162261467 % n is 0


if __name__ == '__main__':
    s = Solution()
    print(s.f2(15))
    print(s.f2(-9))
    print(s.f2(9))
    print(s.f2(3))
    print(s.f2(0))
    print(s.f2(1))
