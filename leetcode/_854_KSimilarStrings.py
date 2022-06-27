import collections
import itertools
from functools import cache

type_pair = tuple[str, str]


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:  # noqa
        """TLE"""
        if s1 == s2: return 0  # noqa: E701
        chars = "abcdef"  # noqa
        n = len(s1)
        pairs = [(a, b) for a in chars for b in chars if a != b]
        index = {p: i for i, p in enumerate(pairs)}

        count = [0] * len(index)
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                count[index[c1, c2]] += 1

        seen: set[type_pair] = set()  # 可能的组合顺序
        for size in range(2, 7):
            for cand in itertools.permutations(chars, size):
                i = cand.index(min(cand))
                seen.add(cand[i:] + cand[:i])

        possibles = []  # 每一个元素 必须同时在count中出现
        for cand in seen:
            row = [0] * len(index)
            for a, b in zip(cand, cand[1:] + cand[:1]):
                row[index[a, b]] += 1
            possibles.append(row)

        zero = tuple([0] * len(index))
        memo = {zero: 0}

        def solve(_count):
            """
            返回 _count 使用 possibles 分组的最大分组数
            """
            if _count in memo: return memo[_count]  # noqa: E701
            ans = 0
            for cycle in possibles:
                count2 = list(_count)
                for i, x in enumerate(cycle):  # 尝试 count2 = count - cycle
                    if count2[i] >= x:
                        count2[i] -= x
                    else:
                        break
                else:
                    ans = max(ans, 1 + solve(tuple(count2)))
            memo[_count] = ans
            return ans

        # 分组大小为m需要移动m-1次
        return sum(count) - solve(tuple(count))

    def kSimilarity2(self, s1: str, s2: str) -> int:  # noqa
        """BFS"""

        def neighbors(string):
            for i, c in enumerate(string):
                if c != s2[i]:
                    break

            chars_s = list(S)
            for j in range(i + 1, len(S)):  # noqa
                if S[j] == s2[i]:
                    chars_s[i], chars_s[j] = chars_s[j], chars_s[i]
                    yield "".join(chars_s)
                    chars_s[j], chars_s[i] = chars_s[i], chars_s[j]

        queue = collections.deque([s1])
        seen = {s1: 0}
        while queue:
            S = queue.popleft()  # noqa
            if S == s2: return seen[S]  # noqa: E701
            for T in neighbors(S):
                if T not in seen:
                    seen[T] = seen[S] + 1
                    queue.append(T)


if __name__ == "__main__":
    s = Solution()
    y = s.kSimilarity2("aaaabbbbccccddddeeee", "bddceeceababeccddaab")
    print(y)
