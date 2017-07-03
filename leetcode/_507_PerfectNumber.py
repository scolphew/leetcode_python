class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False
        ans = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                ans += i + num // i
            i += 1
        return ans == num


if __name__ == '__main__':
    s = Solution()
    print(s.checkPerfectNumber(28))
