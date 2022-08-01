class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:  # noqa
        size = 0
        for char in s:
            if char.isdigit():
                size *= int(char)
            else:
                size += 1

        for char in reversed(s):
            k %= size
            if k == 0 and char.isalpha():  # 为0则意味着求当前的最后一位
                return char
            if char.isdigit():
                size //= int(char)
            else:
                size -= 1


if __name__ == '__main__':
    s = Solution()
    x = s.decodeAtIndex("abc2d", 2)
    print(x)
