from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:  # noqa
        ans = []
        x = 0
        for i in range(len(s) - 1, -1, -1):
            x = (x + shifts[i]) % 26
            c = ord(s[i]) + x
            if c > ord('z'):
                c -= 26
            ans.append(chr(c))
        return ''.join(ans[::-1])


if __name__ == "__main__":
    s = Solution()
    ss = ""
    ls = []
    for i in range(30):
        ss += 'a'
        ls.append(1)
    y = s.shiftingLetters(ss, ls)
    print(y)
