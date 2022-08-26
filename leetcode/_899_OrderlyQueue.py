class Solution:
    def orderlyQueue(self, ss: str, k: int) -> str:  # noqa
        if k == 1:
            n = len(ss)
            x = ss + ss[:-1]
            for i in range(1, n):
                ss = min(ss, x[i:i + n])
            return ss
        return ''.join(sorted(ss))


if __name__ == "__main__":
    s = Solution()
    y = s.orderlyQueue("cba", 1)
    print(y)
