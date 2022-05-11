from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:  # noqa
        d = [
            ".-", "-...", "-.-.", "-..", ".",
            "..-.", "--.", "....", "..", ".---",
            "-.-", ".-..", "--", "-.", "---",
            ".--.", "--.-", ".-.", "...", "-",
            "..-", "...-", ".--", "-..-", "-.--",
            "--..",
        ]
        return len(set("".join(d[ord(c) - ord('a')] for c in word) for word in words))


if __name__ == '__main__':
    s = Solution()
    x = s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
    print(x)
