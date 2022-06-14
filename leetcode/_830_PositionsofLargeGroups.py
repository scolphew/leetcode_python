from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:  # noqa
        ans = []
        start = 0
        for i, ch in enumerate(s):
            if ch != s[start]:
                if i - start >= 3:
                    ans.append([start, i - 1])
                start = i
        else:
            if i - start >= 2:
                ans.append([start, i])
        return ans


if __name__ == '__main__':
    s = Solution()
    x = s.largeGroupPositions("a")
    print(x)
