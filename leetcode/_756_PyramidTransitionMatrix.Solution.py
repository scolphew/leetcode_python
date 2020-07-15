from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        from collections import defaultdict
        d = defaultdict(set)
        for a, b, c in allowed:
            d[a, b].add(c)

        def dfs(A):
            level = len(A)
            if level == 1:
                return True
            this = [None] * (level - 1)
            i, j = 0, 0
            while i < level - 1:  # 新层第i位
                while j < 7:  # ABCDEFG
                    if chr(65 + j) in d[A[i], A[i + 1]]:  # 能放
                        this[i] = chr(65 + j)
                        j = 0
                        break
                    else:
                        j += 1

                if this[i] is None:  # 没什么可放的
                    if i == 0:
                        break
                    else:
                        i -= 1
                        j = ord(this[i]) - 65 + 1
                        this[i] = None
                        continue
                if i == level - 2:
                    if dfs(this):
                        return True
                    else:
                        j = ord(this[i]) - 65 + 1
                        this[i] = None
                        continue
                i += 1
            return False

        return dfs(bottom)

    def s2(self, bottom, allowed):
        from collections import defaultdict
        T = defaultdict(set)
        for u, v, w in allowed:
            T[u, v].add(w)

        def solve(A):
            if len(A) == 1:
                return True
            return any(solve(cand) for cand in build(A, []))

        def build(A, ans, i=0):
            if i + 1 == len(A):
                yield "".join(ans)
            else:
                for w in T[A[i], A[i + 1]]:
                    ans.append(w)
                    for result in build(A, ans, i + 1):
                        yield result
                    ans.pop()

        return solve(bottom)


if __name__ == '__main__':
    s = Solution()
    print(s.s2("CCC",
               ["CBB", "ACB", "ABD", "CDB", "BDC", "CBC", "DBA",
                "DBB", "CAB", "BCB", "BCC", "BAA", "CCD", "BDD",
                "DDD", "CCA", "CAA", "CCC", "CCB"]))
    print(s.pyramidTransition("AABA", ["AAA", "AAB", "ABA", "ABB", "BAC"]))
    print(s.pyramidTransition("BCD", ["BCG", "CDE", "GEA", "FFF"]))
