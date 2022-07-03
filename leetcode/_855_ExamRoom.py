import heapq


class Interval:
    def __init__(self, start, end, N):
        self.start = start
        self.end = end
        if start == 0 or end == N - 1:
            self.length = end - start
        else:
            self.length = (end - start) // 2

    def __lt__(self, other: 'Interval'):
        return self.start < other.start if self.length == other.length else self.length > other.length

    def __repr__(self):
        return f"{self.start}->{self.end}"


class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.q = [Interval(0, n - 1, n)]  # 最小堆

    def seat(self) -> int:
        a = heapq.heappop(self.q)
        if a.start == 0:
            result = 0
        elif a.end == self.n - 1:
            result = self.n - 1
        else:
            result = a.start + a.length

        if result > a.start:
            t = Interval(a.start, result - 1, self.n)
            heapq.heappush(self.q, t)
        if result < a.end:
            t = Interval(result + 1, a.end, self.n)
            heapq.heappush(self.q, t)
        return result

    def leave(self, p: int) -> None:
        left = right = None
        for i, a in enumerate(self.q):
            if a.start == p + 1:
                right = a
                r = i
            if a.end == p - 1:
                left = a
                l = i
        if left:
            self._remove(self.q.index(left))
        if right:
            self._remove(self.q.index(right))

        heapq.heappush(self.q, Interval(left.start if left else p, right.end if right else p, self.n))

    def _remove(self, i):
        if len(self.q) - 1 == i:
            self.q.pop()
        else:
            q = self.q
            x = q.pop()
            q[i] = x
            heapq._siftup(q, i)


if __name__ == '__main__':
    s = ExamRoom(100)
    print(s.seat())
    print(s.seat())
    print(s.seat())
    print(s.seat())
    print(s.seat())
    print(s.seat())

    s.leave(49)
    print(s.q)
    print(s.seat())
    print(s.q)

    print(s.seat())
    print(s.q)

    print(s.seat())
    print(s.q)

    print(s.seat())
    print(s.q)
