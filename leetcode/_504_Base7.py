class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            return "-" + self.convertToBase7(-num)
        if num == 0:
            return "0"
        ans = ""
        while num > 0:
            num, b = num // 7, num % 7
            ans = str(b) + ans
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.convertToBase7(100))
    print(s.convertToBase7(-100))
    print(s.convertToBase7(1))
    print(s.convertToBase7(0))
    print(s.convertToBase7(-1))
