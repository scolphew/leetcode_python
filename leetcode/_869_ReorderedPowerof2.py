class Solution:
    @staticmethod
    def count(n: int) -> tuple[int]:  # noqa
        cnt = [0] * 10
        while n:
            cnt[n % 10] += 1
            n //= 10
        return tuple(cnt)

    def __init__(self):
        self.f = {self.count(1 << i) for i in range(30)}

    def reorderedPowerOf2(self, n: int) -> bool:  # noqa
        print(self.f)
        print(self.count(n))
        return self.count(n) in self.f


if __name__ == "__main__":
    s = Solution()
    y = s.reorderedPowerOf2(10)
    print(y)
