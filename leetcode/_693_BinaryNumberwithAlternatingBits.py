class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        i = n & 1
        n = n >> 1
        while n:
            i = 1 - i
            if n & 1 != i:
                return False
            n = n >> 1
        return True


if __name__ == '__main__':
    s = Solution()
    for i in range(1, 100):
        print(i, bin(i), s.hasAlternatingBits(i))
