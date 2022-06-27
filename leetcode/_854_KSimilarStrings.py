import itertools
from functools import cache

type_pair = tuple[str, str]


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:  # noqa
        chars = "abcdef"
        N1, N2 = 6, 25  # noqa
        pairs = [(a, b) for a in chars for b in chars if a != b]
        index = {p: i for i, p in enumerate(pairs)}

        count = [0] * len(index)
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                count[index[c1, c2]] += 1

        seen: set[type_pair] = set()  # 可能的组合顺序
        for size in range(2, N1 + 1):
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
            if _count in memo: return memo[_count]
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


if __name__ == "__main__":
    s = Solution()
    y = s.kSimilarity("aaaabbbbccccddddeeee", "bddceeceababeccddaab")
    print(y)
