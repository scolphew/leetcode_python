class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:  # noqa
        def match(s1, s2):
            d1, d2 = {}, {}
            for c1, c2 in zip(s1, s2):
                x1, x2 = c1 in d1, c2 in d2
                if x1 == x2:
                    if x1 and (d1[c1] != c2 or d2[c2] != c1):  # 都在 判断
                        return False
                    else:  # 都不在 添加
                        d1[c1] = c2
                        d2[c2] = c1
                else:
                    return False

            return True

        return [word for word in words if match(word, pattern)]


if __name__ == "__main__":
    s = Solution()
    y = s.findAndReplacePattern(words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb")
    print(y)
