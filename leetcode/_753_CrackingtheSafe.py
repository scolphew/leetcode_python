class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        ans = "0" * (n - 1)
        s = set()
        for _ in range(k ** n):
            prev = ans[-n + 1:] if n > 1 else ''
            for j in map(str, range(k - 1, -1, -1)):
                now = prev + j
                if now not in s:
                    s.add(now)
                    ans += j
                    break
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.crackSafe(3, 3))
