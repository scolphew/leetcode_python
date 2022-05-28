from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:  # noqa
        from collections import defaultdict
        banned = set(banned)
        banned.add("")
        stop_word = set("!?',;. ")
        start = 0
        words = defaultdict(int)
        ans, count = "", 0
        for i, c in enumerate(paragraph):
            if c in stop_word:
                tmp = paragraph[start:i].lower()
                words[tmp] += 1
                start = i + 1
                if words[tmp] > count and tmp not in banned:
                    ans, count = tmp, words[tmp]
        else:
            tmp = paragraph[start:].lower()
            words[tmp] += 1
            if words[tmp] > count and tmp not in banned:
                ans, count = tmp, words[tmp]
        return ans


if __name__ == '__main__':
    s = Solution()
    x = s.mostCommonWord("Bob", ["hit"])
    print(x)
