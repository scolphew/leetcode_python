import itertools
from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:  # noqa
        def make(frag):
            n = len(frag)
            for d in range(1, n + 1):
                left, right = frag[:d], frag[d:]
                if (not left.startswith('0') or left == '0') \
                        and not right.endswith('0'):
                    yield f"{left}{'.' if d != n else ''}{right}"

        s = s[1:-1]
        return [f"({cand[0]}, {cand[1]})"
                for i in range(1, len(s))
                for cand in itertools.product(make(s[:i]), make(s[i:]))]


if __name__ == '__main__':
    so = Solution()
    x = so.ambiguousCoordinates("(12345)")
    print(x)
