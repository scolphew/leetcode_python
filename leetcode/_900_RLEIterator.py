class RLEIterator:

    def __init__(self, encoding: list[int]):
        self.nums = encoding
        self.i = 0
        self.q = 0

    def next(self, n: int) -> int:
        while self.i < len(self.nums):
            if self.q + n <= self.nums[self.i]:
                self.q += n
                return self.nums[self.i + 1]
            else:
                n -= self.nums[self.i] - self.q
                self.q = 0
                self.i += 2
        return -1


if __name__ == '__main__':
    s = RLEIterator([3, 8, 0, 9, 2, 5])
    print(s.next(1))
    print(s.next(4))
    print(s.next(1))
