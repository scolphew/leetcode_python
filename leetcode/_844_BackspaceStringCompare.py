class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:  # noqa
        i, j = len(s) - 1, len(t) - 1
        a = b = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    i -= 1
                    a += 1
                elif a > 0:
                    a -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == "#":
                    j -= 1
                    b += 1
                elif b > 0:
                    j -= 1
                    b -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if s[i] != t[j]: return False
            elif i >= 0 or j >= 0:  # 其中一个到头了
                return False
            i -= 1
            j -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    y = s.backspaceCompare("bbbextm",
                           "bbb#extm")
    print(y)
