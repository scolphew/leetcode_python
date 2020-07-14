import collections
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0

        target = int(target)

        visited = set(int(i) for i in deadends)

        if target in visited or 0 in visited:
            return -1

        que = collections.deque()
        visited.add(0)
        que.append(0)
        step = 0

        def help(p):
            if p == target:
                return True
            if p not in visited:
                que.append(p)
                visited.add(p)

        while que:
            step += 1
            size = len(que)
            for i in range(size):
                point = que.popleft()
                for each in (1, 10, 100, 1000):
                    newPoint = (point + each) if (
                            point // each % 10 != 9) else (point - 9 * each)
                    if help(newPoint):
                        return step
                    newPoint = (point - each) if (
                            point // each % 10 != 0) else (point + 9 * each)
                    if help(newPoint):
                        return step
        return -1

    def openLock2(self, deadends: List[str], target: str) -> int:
        def dist(code):
            return sum(min(int(c), 10 - int(c)) for c in code)

        def neighbors(code):
            for i in range(4):
                x = int(code[i])
                yield code[:i] + str((x - 1) % 10) + code[i + 1:]
                yield code[:i] + str((x + 1) % 10) + code[i + 1:]

        deadends = set(deadends)
        if '0000' in deadends or target in deadends:
            return -1
        # 最后一步
        last_moves = set(neighbors(target)) - deadends
        if not last_moves:
            return -1
        ans = dist(target)
        for code in last_moves:
            if dist(code) < ans:
                return ans
        return ans + 2


if __name__ == '__main__':
    s = Solution()
    print(s.openLock2(["0201", "0101", "0102", "1212", "2002"], "0202"))
