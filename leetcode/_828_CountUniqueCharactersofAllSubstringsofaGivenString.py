import collections


class Solution:
    def uniqueLetterString(self, s: str) -> int:  # noqa
        def lst():
            return [-1]

        n = len(s)
        M = 10 ** 9 + 7  # noqa
        indices = collections.defaultdict(lst)
        for i, c in enumerate(s):
            indices[c].append(i)

        ans = 0
        for each in indices.values():
            each.append(n)
            for i in range(1, len(each) - 1):
                ans += (each[i] - each[i - 1]) * (each[i + 1] - each[i])
                ans %= M
        return ans


if __name__ == '__main__':
    s = Solution()
    y = s.uniqueLetterString("ABC")
    print(y)
