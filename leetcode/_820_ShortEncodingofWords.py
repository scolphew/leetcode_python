import collections
import pprint
from functools import reduce
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:  # noqa
        words = list(set(words))
        Trie = lambda: collections.defaultdict(Trie)  # noqa
        trie = Trie()

        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)


if __name__ == '__main__':
    s = Solution()
    x = s.minimumLengthEncoding(["time", "me", "bell"])
    print(x)
